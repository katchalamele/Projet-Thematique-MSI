from message import Message
from copy import deepcopy
import inspect

recept = 0

class Entity:
    def __init__(self, uuid, capacity, battery):
        self.uuid = uuid
        self.capacity = capacity
        self.battery = battery
        self.power = battery
        self.messages = []

    def createMsg(self, dest, text):
        msg = Message(self.uuid, dest, text, 50, 0)
        self.messages.append(msg)
    
    def send(self, Entity, msg, t):
        if msg.ttl-1 > 0:
            Entity.receive(deepcopy(msg), t)
        
    def receive(self, msg, t):
        global recept
        if len(self.messages)+1 < self.capacity:
            msg.ttl = msg.ttl - 1
            msg.hp = t
            if (msg.ttl > 0) or (msg.dst == self.uuid):
                for m in self.messages:
                    if (m.uuid == msg.uuid):
                        return
                if msg.dst == self.uuid:
                     if not msg.isOk:
                         recept += 1
                         msg.isOk = True
                self.messages.append(msg)
               
                
            
    
    #Routine journaliere supprime tout msg expiré en tps
