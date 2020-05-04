from Params import TTL

counter = 0

class Message:
    def __init__(self, src, dst, crp, dexp, ttl=TTL):
        global counter
        uuid = counter
        counter += 1
        
        self.uuid = uuid
        self.ttl = ttl
        self.src = src
        self.dst = dst
        self.crp = crp
        self.dexp = dexp
        self.isOk = False
