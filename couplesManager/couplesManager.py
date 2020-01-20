from random import choice

class CouplesManager:
    def __init__(self, node):
        self.couples = []
        self.possibles = [i for i in range(node)]
        
    def generate(self, modifier):
        if(modifier >= 0):
            for i in range(modifier):
                if(len(self.possibles)>1):
                    e1 = choice(self.possibles)
                    self.possibles.remove(e1)
                    e2 = choice(self.possibles)
                    self.possibles.remove(e2)
                    self.couples.append(sorted([e1, e2]))
        else:
            for i in range(0, abs(modifier)):
                if(len(self.couples)>0):
                    e = choice(self.couples)
                    self.couples.remove(e)
                    self.possibles.append(e[0])
                    self.possibles.append(e[1])
