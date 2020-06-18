#Auteurs: Groupe MSI

from random import randint
from Vector import Vector
from lib import random_hex_color,distance
from Params import TAILLE,MMD,DC,R,CP,BT
from message import Message
from copy import deepcopy

class Noeud:
    
    def __init__(self, uuid, capacity=CP, battery=BT):
        self.uuid = uuid
        self.x = randint(0, TAILLE)
        self.y = randint(0, TAILLE)
        self.vect = Vector()
        self.target = None
        self.standby = True
        self.color = random_hex_color()
        self.circle = None
        self.messages = []
        self.capacity = capacity
        self.battery = battery
        self.power = battery
        self.home = None
        self.cpt = None

    def draw(self, canvas):
        self.circle = canvas.create_oval(self.x - R, self.y - R, self.x + R, self.y + R, fill = self.color), canvas.create_text(self.x, self.y, text=str(self.uuid), fill='white')        

    def next_move(self, canvas):
        if not self.standby:
            d = randint(0, MMD)
            #self.vect.rotate()
            dx = self.vect.x * d
            dy = self.vect.y * d
            if 0 < self.x + dx < TAILLE and 0 < self.y + dy < TAILLE :
                self.x += dx
                self.y += dy
                canvas.move(self.circle[0], dx, dy)
                canvas.move(self.circle[1], dx, dy)
                if distance(self, self.target) < DC:
                    self.standby = not self.standby

    def goto(self, lieu):
        self.vect.setXY(lieu.x-self.x, lieu.y-self.y)
        self.vect.normalise()
        self.target = lieu
        self.standby = False
    
    def go_home(self):
        self.goto(self.home)
    

    def createMsg(self, dest, text, dexp):
        msg = Message(self.uuid, dest, text, dexp)
        self.messages.append(msg)
        self.cpt.incr_satur_reseau()
        self.cpt.logger.info("Nouveau message "+str(msg.uuid)+":  "+str(self.uuid)+" =======> "+str(dest))
        
    
    def receive(self, msg):
        if len(self.messages)+1 < self.capacity:
            msg.ttl = msg.ttl - 1
            if (msg.ttl > 0) or (msg.dst == self.uuid):
                for m in self.messages:
                    if (m.uuid == msg.uuid):
                        return
                if msg.dst == self.uuid:
                    self.cpt.logger.info(str(self.uuid)+": Réception de message "+str(msg.uuid)+" provenant de "+str(msg.src))
                    msg.isOk = True
                    self.cpt.incr_recus()
                self.cpt.incr_satur_reseau()
                self.messages.append(msg)
    
    def send_all(self, dst):
        for msg in self.messages:
            if msg.ttl-1 > 0 and not msg.isOk:
                dst.receive(deepcopy(msg))
                #print("noeud", self.uuid, "envoie", msg.uuid, "au noeud", dst.uuid)
    
    def remove_exp_msg(self, clock):
        for msg in self.messages:
            if msg.dexp <= clock:
                self.messages.remove(msg)
                self.cpt.decr_satur_reseau()