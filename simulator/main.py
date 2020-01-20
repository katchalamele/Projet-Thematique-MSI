from json import loads
from message import Message
from entity import Entity
from random import choices
from random import randrange

def main():
    with open('../graphs.json', 'r') as f:
        temporalGraph = [loads(line) for line in f]

    entities = {}
    leng = 0
    ativ = 0
    runt = 0
    for graph in temporalGraph:
        time = graph[0]
        if (len(graph[1])>0):
            edges = choices(graph[1], k=randrange(int(len(graph[1])/2), len(graph[1])+1))
            ativ += len(edges)*100/len(graph[1])
        else:
            edges = []
        print('Temps: ' + str(time) + '/' + str(len(temporalGraph)-1) +
              '  Activés: ' + str(len(edges)) + '/' + str(len(graph[1])))
        runt += 1
        for edge in edges:
            for uuid in edge:
                if not(uuid in entities):
                    entities[uuid] = Entity(uuid)
            #messages echange
                    
            entities[edge[0]].sendAll(entities[edge[1]])
            entities[edge[1]].sendAll(entities[edge[0]])

    ##print(entities)
    res = []
    for e in entities:
        for m in entities[e].messages:
            res.append([e, 'node: ' + str(e) + '  ttl: ' + str(m.ttl)])
    res.sort()
    with open('ttl stat', 'w') as f:
        for e in res:
            f.write(e[1] + '\n')
    print(ativ/runt)
