from random import choices
from random import randrange
from itertools import combinations

#Manage two list of couples with identity in range minimum, maximum, the couples
#selected (couple) and the other (couples_possible)

#Return all couples combinaisons in minimum, maximum identity
def allCouplesCompute(minimum, maximum):
    l = []
    for i in range(minimum, maximum):
        l.append(i)
    couples = []
    for i in combinations(l, 2):
        couples.append(i)
    return(couples)

#Select or remove pseudo randomly couples
def couplesGenerator(modifier, couples, couples_possible):
    couples_removed = []
    if(modifier >= 0):
        for i in range(0, modifier):
            e = choices(couples_possible)
            couples_possible.remove(e[0])
            couples.append(e[0])
    else:
        for i in range(0, abs(modifier)):
            e = choices(couples)
            couples.remove(e[0])
            couples_possible.append(e[0])
            couples_removed.append(e[0])
    couples_removed.sort()
    couples.sort()
    return couples, couples_possible, couples_removed

#Init couples
def init(minimum, maximum):
    all_couple = allCouplesCompute(minimum, maximum)    
    couples_possible = all_couple.copy()
    couples, couples_possible, couples_removed = couplesGenerator(
        randrange(1, len(couples_possible)+1), [], couples_possible)
    return couples, couples_possible
