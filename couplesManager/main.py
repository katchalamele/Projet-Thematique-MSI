from json import dumps
from random import randrange
from couplesManager import CouplesManager
from sys import stdout

def main(NODE = 50, TIME = 100):
    result = {}
    cm = CouplesManager(NODE)
    open('../graphs.json', 'w')
    for t in range(TIME):
        modifier = randrange(-(len(cm.couples)), len(cm.possibles))
        cm.generate(modifier)
        with open('../graphs.json', 'a') as f:
            f.write(dumps([t, sorted(cm.couples)]) + '\n')
        percent = ("{0:." + str(1) + "f}").format((t) * 100/ float(TIME))
        print('\r%s%%' % (percent), end ='\r')
    print('Complete')
