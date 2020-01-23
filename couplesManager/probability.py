from math import sin

def inHour(x):
    return round(((x)/60)%24,2)

def StreetProbability(x):
    return 0.5
    
def WorkProbability(x):
    if x < 12:
        p = round(-0.2 * pow(x-10, 2)+1, 2)
        if p < 0:
            return 0
        return p
    else:
        p = round(-0.2 * pow(x-16, 2)+1, 2)
        if p < 0:
            return 0
        return p

def RestorantProbability(x):
    p = round(-0.1 * pow(x-12.5, 2)+1, 2)
    if p < 0:
        return 0
    return p

def HouseProbability(x):
    return round(-0.4 * sin(-0.262 * x + -1.57)+0.5, 2)

def ResteProbability(x):
    #7-9 12-14 16-19
    if ((x < 7) or
        ((x > 8) and (x < 12)) or
        ((x > 13) and (x < 16)) or
        (x > 18)):
        return 5
    else:
        return 0

def dayProbability():
    dayProb = {'home': [], 'street': [],
               'work': [], 'restorant':[], 'reste':[]}
    for i in range(1440):
        t = inHour(i)
        dayProb['home'].append(HouseProbability(t))
        dayProb['street'].append(StreetProbability(t))
        dayProb['work'].append(WorkProbability(t))
        dayProb['restorant'].append(RestorantProbability(t))
        dayProb['reste'].append(ResteProbability(t))
    return dayProb


##town[0-9]*-street
##city[0-9]*-mainstreet[0-9]*
##city[0-9]*-town[0-9]*-street
##city[0-9]*-place-street
##city[0-9]*-work[0-9]*-street
##city[0-9]*-work[0-9]*-restorant[0-9]*
##city[0-9]*-work[0-9]*-enterprise[0-9]*
##city[0-9]*-place-enterprise[0-9]*
##city[0-9]*-place-restorant[0-9]*
##city[0-9]*-town[0-9]*-house[0-9]*
##town[0-9]*-house[0-9]*
#24*60 = 1440
