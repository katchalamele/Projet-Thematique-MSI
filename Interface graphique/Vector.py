#Auteur: KATCHALA MELE Daouda

from random import randint
from math import cos,sin,radians
from Params import MA

class Vector:

    def __init__(self):
        self.x = randint(-1, 1)
        self.y = randint(-1, 1)

    def rotate(self):
        a = radians(randint(-MA, MA))
        self.x, self.y = (self.x)*cos(a) - (self.y)*sin(a), (self.x)*sin(a) + (self.y)*cos(a)
