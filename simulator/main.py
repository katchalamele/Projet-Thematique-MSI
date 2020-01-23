from json import loads
from message import Message
from entity import Entity
from random import choices
from random import randrange

with open('../graphs.json', 'r') as f:
    temporalGraph = [loads(line) for line in f]

First = True
entities = {}
leng = 0
ativ = 0
runt = 0
for time in range(len(temporalGraph)):
    graph = temporalGraph[time]   
##    if (len(graph)>0):
##        edges = choices(graph, k=randrange(int(len(graph)/2), len(graph)+1))
##        ativ += len(edges)*100/len(graph)
##    else:
##        edges = []
##    print('Temps: ' + str(time) + '/' + str(len(temporalGraph)-1) +
##          '  Activés: ' + str(len(edges)) + '/' + str(len(graph)))
##    runt += 1
    for edge in graph:
        for uuid in edge:
            if not(uuid in entities):
                entities[uuid] = Entity(uuid, First)
                if First:
                    First = not(First)
        #messages echange    
        entities[edge[0]].sendAll(entities[edge[1]], time)
        entities[edge[1]].sendAll(entities[edge[0]], time)

    percent = ("  {0:." + str(1) + "f}").format((time+1) * 100/ float(len(temporalGraph)))
    print('\r%s%%' % (percent), end ='\r')

##print(entities)
res = []
ttl = 50
hp = 0
a = 0
for e in entities:
    for m in entities[e].messages:
        res.append([e, 'node: ' + str(e) + '  ttl: ' + str(m.ttl) + '  t: ' + str(m.hp)])
        if m.ttl < ttl:
            ttl = m.ttl
        if m.hp > hp:
            hp = m.hp
        a += 1
res.sort()
with open('out.txt', 'w') as f:
    for e in res:
        f.write(e[1] + '\n')
    f.write('e: '+ str(a) + '/' + str(len(entities))+'  ttl>: '+str(ttl)+'  t<: '+str(hp))
##print(ativ/runt)
