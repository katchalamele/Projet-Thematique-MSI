from json import dumps
from random import randrange
import couplesManager as cm


NODE = 10
T = 10
result = {}

couples, possibles = cm.init(1, NODE)
result['t0'] = couples.copy()

for i in range(0, T-1):
    modifier = randrange(-(len(couples)), len(possibles))
    couples, possibles, removed = cm.couplesGenerator(
        modifier, couples, possibles)
    result['t'+str(i+1)] = couples.copy()
    
with open('graphs.json', 'w') as f:
    f.write(dumps(result, indent=4))
