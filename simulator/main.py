import configparser
from json import loads
from message import Message
import entity 
import random
import string
import threading

connexion = 0
possiblesend = 0
sendnb = 0
unsended = 0

def edgeExchange(edge):
    global connexion
    global possiblesend
    global sendnb
    global unsended
    perte = random.randrange(int(config['CONNEXION']['PourcentagePerteMin']),
                int(config['CONNEXION']['PourcentagePerteMax'])) or 1
    connexion += 1
    for e in range(len(edge)):
        for m in entities[edge[e]].messages:
            possiblesend += 1
            if random.random() < 1-(perte)/100:
                sendnb += 1
                entities[edge[e]].send(entities[edge[(e+1)%2]], m, time)
            else:
                unsended += 1


config = configparser.ConfigParser()
config.read('config.ini')

with open('../graphs.json', 'r') as f:
    print(' File Load...', end='\r')
    temporalGraph = [loads(line) for line in f]
    print(' File Load. OK')


print(' Parameters Load...', end='\r')
entities = {}
for time in range(len(temporalGraph)):
    graph = temporalGraph[time]   
    for edge in graph:
        for uuid in edge:
            if not(uuid in entities):
                capa = random.randrange(int(config['NOEUD']['CapaciteMin']),
                    int(config['NOEUD']['CapaciteMax']))
                bat = random.randrange(int(config['NOEUD']['BatterieMin']),
                    int(config['NOEUD']['BatterieMax']))
                entities[uuid] = entity.Entity(uuid, capa, bat)
    percent = ("{0:." + str(1) + "f}").format((time+1) * 100/ float(len(temporalGraph)))
    print('Parameters Load... %s%%             ' % (percent), end='\r')
print(' Parameters Load. OK         ')

print(' Message Generation...', end='\r')
msg = {}
nbmsg = range(int(config['MESSAGE']['NombreMessages']))
for m in nbmsg:
    key = random.randrange(len(temporalGraph))
    if key not in msg:
        msg = {**msg, key:[]}
    msg[key].append((
        random.sample(range(len(entities)), 2),
        ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])))
    percent = ("{0:." + str(1) + "f}").format((m+1) * 100/ float(len(nbmsg)))
    print('Message Generation... %s%%' % (percent), end='\r')
print(' Message Generation. Ok        ')



print(' Exchange Simulation...', end='\r')
for time in range(len(temporalGraph)):
    graph = temporalGraph[time]
    if time in msg:
        for m in msg[time]:
            entities[m[0][0]].createMsg(m[0][1], m[1])
    threads = []
    for edge in graph:
        x = threading.Thread(target=edgeExchange, args=(edge,))
        threads.append(x)
        x.start()
    for t in range(len(graph)):
        threads[t].join()
    percent = ("{0:." + str(1) + "f}").format((time+1) * 100/ float(len(temporalGraph)))
    print(' Exchange Simulation... %s%%' % (percent), end='\r')
print(' Exchange Simulation. Ok       ')

capacityoverload = 0
ttlmoyenne = 0
msg = 0
hpmoyenne = 0
print(' Rapport Generation...', end='\r')
nodesize = len(str(len(entities)))
msgsize = len(config['MESSAGE']['NombreMessages'])
capasize = len(config['NOEUD']['CapaciteMax'])
powersize = len(config['NOEUD']['BatterieMax'])
rapport = ''
rapport +='Node : Capacité Power\n'
rapport +='{0:{size}}'.format(' ', size=nodesize)+'MessageID Source Destination Corps TTL HP\n'
for e in entities:
    rapport += ('{0:{size}}'.format(entities[e].uuid, size=nodesize)+':\t'+
          '{0:{size}}'.format(len(entities[e].messages), size=msgsize)+'/'+'{0:{size}}'.format(entities[e].capacity, size=capasize)+'\t'+
          '{0:{size}}'.format(entities[e].power, size=powersize)+'/'+'{0:{size}}'.format(entities[e].battery, size=powersize)+'\n')
    capacityoverload += (len(entities[e].messages)*100)/(entities[e].capacity or 1)
    for m in entities[e].messages:
        ttlmoyenne += m.ttl
        msg += 1
        hpmoyenne += m.hp
        rapport +=('{0:{size}}'.format(' ', size=nodesize+2)+
              '{0:{size}}'.format(m.uuid, size=msgsize)+' '+
              '{0:{size}}'.format(m.src, size=nodesize) +' '+
              '{0:{size}}'.format(m.dst, size=nodesize) +' '+
              '{0:16}'.format(m.crp)+' '+str(m.ttl) +' '+ str(m.hp)+'\n')
capacityoverload = capacityoverload / len(entities)
rapport +='Total connexion: '+ str(connexion) +' \t Send statistique: ' + str(sendnb) + '/' + str(unsended) + '/' + str(possiblesend)+'\n'
rapport +='Overcharge: '+str(capacityoverload) +'\t TTL moyenne: ' + str(ttlmoyenne/msg) +' \t HP moyenne: ' + str(hpmoyenne/msg) +'\n'
rapport +='Total Arrivée: '+str(entity.recept)+"/"+str(config['MESSAGE']['NombreMessages'])
with open('../rapport.txt', 'w') as f:
    f.write(rapport)
print(' Rapport Generation. OK  ')
print('DONE')
