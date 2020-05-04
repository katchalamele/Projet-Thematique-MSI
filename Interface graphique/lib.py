from random import randint
from math import sqrt

def random_hex_color():
    r = str(hex(randint(0,255)))[2:]
    g = str(hex(randint(0,255)))[2:]
    b = str(hex(randint(0,255)))[2:]
    if len(r) < 2: r = '0' + r
    if len(g) < 2: g = '0' + g
    if len(b) < 2: b = '0' + b
    return '#'+r+g+b

def distance(p1, p2):
    return sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))
