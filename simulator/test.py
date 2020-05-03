import configparser
import random
from message import Message


config = configparser.ConfigParser()
config.read('config.ini')

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
