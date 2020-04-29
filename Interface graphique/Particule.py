#Auteur: KATCHALA MELE Daouda

from random import randint
from Vector import Vector
from lib import random_hex_color
from Params import *

class Particule:
    
    def __init__(self, pid):
        self.pid = pid
        self.x = randint(0, TAILLE)
        self.y = randint(0, TAILLE)
        self.vect = Vector()
        self.color = random_hex_color()
        self.circle = None

    def draw(self, canvas):
        self.circle = canvas.create_oval(self.x - R, self.y - R, self.x + R, self.y + R, fill = self.color), canvas.create_text(self.x, self.y, text=str(self.pid), fill='white')        

    def next_move(self, canvas):
        d = randint(0, MMD)
        self.vect.rotate()
        dx = self.vect.x * d
        dy = self.vect.y * d
        if 0 < self.x + dx < TAILLE and 0 < self.y + dy < TAILLE :
            self.x += dx
            self.y += dy
            canvas.move(self.circle[0], dx, dy)
            canvas.move(self.circle[1], dx, dy)
