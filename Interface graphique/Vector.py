#Auteur: KATCHALA MELE Daouda

from random import randint
from math import cos,sin,radians,sqrt
from Params import MA

class Vector:

    def __init__(self, x = randint(-1, 1), y = randint(-1, 1)):
        self.x = x
        self.y = y

    def rotate(self):
        a = radians(randint(-MA, MA))
        self.x, self.y = (self.x)*cos(a) - (self.y)*sin(a), (self.x)*sin(a) + (self.y)*cos(a)

    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    def normalise(self):
        n = self.norme()
        self.x,self.y = self.x/n, self.y/n

    def norme(self):
        return sqrt((self.x**2) + (self.y**2))
    
