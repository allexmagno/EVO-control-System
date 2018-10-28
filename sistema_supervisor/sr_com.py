import Pyro4


@Pyro4.expose
class SRCom:

    def __init__(self, mac, pos):
        self.mac = mac
        self.pos = pos

    def getID(cls):
        return cls.mac

    def getPosInicial(self):
        return self.pos

    def getSituacaoMapa(cls):
        pass

    def setMover(cls, direcao):
        pass

    def setTime(cls):
        pass