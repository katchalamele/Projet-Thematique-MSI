from json import dumps
from random import randrange
import couplesManager as cm
import graphsManager as gm

NODE = 10
T = 10
result = {}

couples, possibles = cm.init(1, NODE)
result['t0'] = couples.copy()
gm.save_graph('t0', NODE, couples)

for i in range(0, T-1):
    modifier = randrange(-(len(couples)), len(possibles))
    couples, possibles, removed = cm.couplesGenerator(
        modifier, couples, possibles)
    result['t'+str(i+1)] = couples.copy()
    gm.save_graph('t'+str(i+1), NODE, couples)
    
with open('graphs.json', 'w') as f:
    f.write(dumps(result, indent=4))
