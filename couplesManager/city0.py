import uuid
#import probability
from random import shuffle
import re

MAISON = 0

def Build(name, n=0):
    #return {name: [[], [uuid.uuid4().hex for i in range(n)]]}
    global MAISON
    ns = []
    for i in range(n):
        ns.append(MAISON)
        MAISON +=1
    return {name: [[], ns]}

def HomeDistrict(name, n, redist):
    dist = {}
    edge = []
    if redist == 0:
        tempn = n // 1
    else:
        tempn = n // redist
    dist[name+'-street'] = [[], []]
    for i in range(tempn):
        dist = {**dist, **Build(name+'-house'+str(i), redist)}
        dist[name+'-street'][0].append([name+'-street', name+'-house'+str(i)])
        dist[name+'-house'+str(i)][0].append([name+'-house'+str(i), name+'-street'])
        edge.append([name+'-street', name+'-house'+str(i)])
    if (redist != 0):
        if (n%redist !=0):
            dist = {**dist, **Build(name +'-house'+str(tempn), +n%redist)}
            dist[name+'-street'][0].append([name+'-street', name+'-house'+str(tempn)])
            dist[name+'-house'+str(tempn)][0].append([name+'-house'+str(tempn), name+'-street'])
            edge.append([name+'-street', name+'-house'+str(tempn)])
    return dist, edge

def WorkDistrict(name, n, streetName, size):
    dist = {}
    edge = []
    r = []
    if size == 0:
        tempn = n // 1
    else:
        tempn = n//size
    dist[name+'-street'] = [[], []]
    r.append(name+'-street')
    for i in range(tempn):
        dist = {**dist, **Build(name+'-enterprise'+str(i))}
        dist[name+'-'+streetName][0].append([name+'-'+streetName, name+'-enterprise'+str(i)])
        dist[name+'-enterprise'+str(i)][0].append([name+'-enterprise'+str(i), name+'-'+streetName])
        edge.append([name+'-'+streetName, name+'-enterprise'+str(i)])
        r.append(name+'-enterprise'+str(i))
    for i in range(tempn-1):
        dist = {**dist, **Build(name+'-restorant'+str(i))}
        dist[name+'-'+streetName][0].append([name+'-'+streetName, name+'-restorant'+str(i)])
        dist[name+'-restorant'+str(i)][0].append([name+'-restorant'+str(i), name+'-'+streetName])
        edge.append([name+'-'+streetName, name+'-restorant'+str(i)])
        r.append(name+'-enterprise'+str(i))
    return dist, edge, r
    
def City(name, n):
    MAISON = 0
    dist = {}
    edge = []
    cityStreet = []
    
    #CREATE TOWN
    townRedist = 5
    demi = n // 2
    redist = demi // townRedist
    rest = n%2 + demi%townRedist
    for town in range(townRedist):
        distTmp, edgeTmp = HomeDistrict('town'+str(town), redist, 2)
        dist = {**dist, **distTmp}
        edge += edgeTmp
        dist[name+'-mainstreet'+str(town)] = [[], []]
        dist[name+'-mainstreet'+str(town)][0].append([name+'-mainstreet'+str(town), 'town'+str(town)+'-street'])
        dist['town'+str(town)+'-street'][0].append(['town'+str(town)+'-street', name+'-mainstreet'+str(town)])
        edge.append([name +'-mainstreet' + str(town), 'town'+str(town)+'-street'])
        cityStreet.append(name+'-mainstreet'+str(town))
    if (rest > 0):
        distTmp, edgeTmp = HomeDistrict('town'+str(townRedist), rest, 2)
        dist = {**dist, **distTmp}
        edge += edgeTmp
        dist[name+'-mainstreet'+str(townRedist)] = [[], []]
        dist[name+'-mainstreet'+str(townRedist)][0].append([name+'-mainstreet'+str(townRedist), 'town'+str(townRedist)+'-street'])
        dist['town'+str(townRedist)+'-street'][0].append(['town'+str(townRedist)+'-street', name+'-mainstreet'+str(townRedist)])
        edge.append([name +'-mainstreet' + str(townRedist), 'town'+str(townRedist)+'-street'])
        cityStreet.append(name+'-mainstreet'+str(townRedist))
        
    #CREATE CITYHOMEDISTRICT
    townRedist = 3
    redist = demi // townRedist
    rest = demi % townRedist
    for town in range(townRedist):
        distTmp, edgeTmp = HomeDistrict(name+'-town'+str(town), redist, 10)
        dist = {**dist, **distTmp}
        edge += edgeTmp
        cityStreet.append(name+'-town'+str(town)+'-street')
    if (rest > 0):
        distTmp, edgeTmp = HomeDistrict(name+'-town'+str(townRedist), rest, 10)
        dist = {**dist, **distTmp}
        edge += edgeTmp
        cityStreet.append(name+'-town'+str(townRedist)+'-street')

    #CREATE WORKDIST
    workRedist = 4
    worksize = 25
    for work in range(workRedist):
        distTmp, edgeTmp, r = WorkDistrict(name+'-work'+str(work), n, 'street', worksize)
        dist = {**dist, **distTmp}
        shuffle(r)
        #connect workbuilding in unclosed circular graph
        for b in range(len(r)-1):
            edgeTmp.append([r[b], r[b+1]])
            dist[r[b]][0].append([r[b], r[b+1]])
            dist[r[b+1]][0].append([r[b+1], r[b]])
        edge += edgeTmp
        cityStreet.append(name+'-work'+str(work)+'-street')

    #CREATE PLACE
    distTmp, edgeTmp, r = WorkDistrict(name+'-place', n, 'street', worksize)
    dist = {**dist, **distTmp}
    for s in cityStreet:
        if re.search(r'city[0-9]*-mainstreet[0-9]*' ,s):
            edgeTmp.append([name+'-place-street', s])
            dist[name+'-place-street'][0].append([name+'-place-street', s])
            dist[s][0].append([s, name+'-place-street'])
    edge += edgeTmp

    #CONNECT ALL CITY STREET IN CIRCULAR GRAPH
    shuffle(cityStreet)
    for s in range(len(cityStreet)-1):
        edge.append([cityStreet[s], cityStreet[s+1]])
        dist[cityStreet[s]][0].append([cityStreet[s], cityStreet[s+1]])
        dist[cityStreet[s+1]][0].append([cityStreet[s+1], cityStreet[s]])
    edge.append([cityStreet[len(cityStreet)-1], cityStreet[0]])
    dist[cityStreet[len(cityStreet)-1]][0].append([cityStreet[len(cityStreet)-1], cityStreet[0]])
    dist[cityStreet[0]][0].append([cityStreet[0], cityStreet[len(cityStreet)-1]])
    
    return dist, edge
