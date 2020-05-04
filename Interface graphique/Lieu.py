#Auteur: KATCHALA MELE Daouda

from random import randint
from lib import random_hex_color
from Params import TAILLE,RL

class Lieu:
    
    def __init__(self, lid, type, frlib, x=None, y=None):
        """
        lid     => Id du lieu à créer
        type    => Type du lieu (gare, Lieu de travail, etc)
        frlib   => Nom du lieu à afficher
        """
        self.lid = lid
        self.type = type
        self.frlib = frlib
        if x is None and y is None: self.x,self.y = randint(0, TAILLE),randint(0, TAILLE)
        else: self.x,self.y = x,y
        self.circle = None

    def draw(self, canvas):
        if self.type == "Domicile":
            self.circle = canvas.create_rectangle(self.x - (RL/3), self.y - (RL/3), self.x + (RL/3), self.y + (RL/3), fill='blue'), canvas.create_text(self.x, self.y, text=str(self.frlib), fill='black')            
        else:
            self.circle = canvas.create_oval(self.x - RL, self.y - RL, self.x + RL, self.y + RL, fill='white'), canvas.create_text(self.x, self.y, text=str(self.frlib), fill='black')       
