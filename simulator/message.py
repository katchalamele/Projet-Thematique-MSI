class Message:
    def __init__(self, uuid, ttl, hp, src, dst, crp):
        self.uuid = uuid
        self.ttl = ttl
        self.hp = hp
        self.src = src
        self.dst = dst
        self.crp = crp
