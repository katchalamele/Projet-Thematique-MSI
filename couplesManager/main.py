import city0
import probability
import re
from random import choices
from random import shuffle
from json import dumps
from sys import argv

#create city, generate prob table, merge two  and return city & list of entities
#with location
def init(n):
    prob = probability.dayProbability()
    city, edge = city0.City('city0', n)
    entities = []
    for k in city.keys():
        if (re.search(r'town[0-9]*-house[0-9]*', k) or
            re.search(r'city[0-9]*-town[0-9]*-house[0-9]*', k)) :
            for e in city[k][1]:
                entities.append([e, k])
            city[k].append(prob['home'])
            
        elif (re.search(r'city[0-9]*-work[0-9]*-enterprise[0-9]*' ,k) or
              re.search(r'city[0-9]*-place-enterprise[0-9]*', k)) :
            city[k].append(prob['work'])
        elif (re.search(r'city[0-9]*-work[0-9]*-restorant[0-9]*' ,k) or
              re.search(r'city[0-9]*-place-restorant[0-9]*', k)) :
            city[k].append(prob['restorant'])
        else:
            city[k].append(prob['street'])
    entities.sort()
    return city, entities, prob['reste']

def scale(val, src, dst):
    return ((val - src[0]) / ((len(src)-1)-src[0])) * ((len(dst)-1)-dst[0]) + dst[0]


print("Please send numbers of entities you want")
n = int(input('n = '))

print("[1/5] City graph compute...")
#city key: [edge, entity, probability(sur 1440min)]
city, entities, prob = init(n)
print("  City graph build")
n = None

print("[2/5] Move graph compute...")
voyage = {}
for e in entities:
    voyage = {**voyage, e[0]: []}
    voyage[e[0]].append(e[1])
for i in range(1440):
    j = int(scale(i, range(1440), range(1440)))
    for e in entities:
        p = [[], []]
        p[0].append(e[1])
        if (re.search(r'street', e[1])):
            p[1].append(0.01)
        else:
            p[1].append(prob[j])
            
        for c in city[e[1]][0]:
            p[0].append(c[1])
            p[1].append(city[c[1]][2][j])
        e[1] = choices(p[0], weights=p[1])[0]
        
        voyage[e[0]].append(e[1])
    percent = ("  {0:." + str(1) + "f}").format((i+1) * 100/ float(1440))
    print('\r%s%%' % (percent), end ='\r')
city = None
prob = None
print("  Move graph complete")


print("[3/5] Entity regroupment...")
lieux = []
for ei in range(len(entities)):
    e = entities[ei]
    for i in range(len(voyage[e[0]])):
        lieux.append({})
        if voyage[e[0]][i] not in lieux[i].keys():
            lieux[i] = {**lieux[i], voyage[e[0]][i]: []}
        lieux[i][voyage[e[0]][i]].append(e[0])
    percent = ("  {0:." + str(1) + "f}").format((ei+1) * 100/ float(len(entities)))
    print('\r%s%%' % (percent), end ='\r')
print("  Entity grouped") 
lengthVoyage = len(voyage[e[0]])
voyage = None
entities = None

print("[4/5] Couple compute...")
temporalGraph = []
for i in range(lengthVoyage):
    temporalGraph.append([])
    for k in lieux[i].keys():
        if not(re.search(r'street', k)):
            shuffle(lieux[i][k])
            l = len(lieux[i][k])
            if l > 1:
                for j in range(1, l, 2):
                    temporalGraph[i].append([lieux[i][k][j-1], lieux[i][k][j]])
        
    temporalGraph[i].sort()
    percent = ("  {0:." + str(1) + "f}").format((i+1) * 100/ float(lengthVoyage))
    print('\r%s%%' % (percent), end ='\r')
print("  Couple compute complete") 
lieux = None

print("[5/5] JSON dump")
open('../graphs.json', 'w')
with open('../graphs.json', 'a') as f:
    for i in range(len(temporalGraph)):
        f.write(dumps(temporalGraph[i]) + '\n')
        percent = ("  {0:." + str(1) + "f}").format((i+1) * 100/ float(len(temporalGraph)))
        print('\r%s%%' % (percent), end ='\r')
print("All complete!")
