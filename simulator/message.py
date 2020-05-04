counter = 0

class Message:
    def __init__(self, src, dst, crp, ttl, hp):
        global counter
        uuid = counter
        counter += 1
        
        self.uuid = uuid
        self.ttl = ttl
        self.hp = hp
        self.src = src
        self.dst = dst
        self.crp = crp
        self.isOk = False
