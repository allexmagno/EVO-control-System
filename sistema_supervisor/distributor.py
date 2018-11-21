from threading import Thread, Event, Lock



class Distributor(Thread):


    def __init__(self, robo, x, y):
        super(Distributor, self).__init__()

        self._robo = robo
        self.x = x
        self.y = y

        self.validar = False

        self.obstaculo = False

    def getNome(self):
        return self.robo

    def getCoord(self):
        return self.x, self.y

    def getY(self):
        return self.y

    def getValidacao(self):
        return self.validar

    def getObstaculo(self):
        return self.obstaculo

    def setValidacao(self, validacao):
        self.validar = validacao

    def setCoord(self, x, y):
        self.x = x
        self.y = y
