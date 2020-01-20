from message import Message
from copy import deepcopy
import inspect

class Entity:
    def __init__(self, uuid):
        self.uuid = uuid
        self.messages = []
        if (uuid == 0):
            msg = Message(1, 50, 0, uuid, 10, "TEST 00")
            self.messages.append(msg)
    
    def send(self, entity, msg):
        entity.receive(msg)

    def sendAll(self, Entity):
        for msg in self.messages:
            Entity.receive(deepcopy(msg))
        
    def receive(self, msg):
        msg.ttl = msg.ttl - 1
        if (msg.ttl > 0) or (msg.dst == self.uuid):
            for m in self.messages:
                if (m.uuid == msg.uuid):
                    return
            self.messages.append(msg)
            
    
    #Routine journaliere supprime tout msg expiré en tps
