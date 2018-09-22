


class Coordenadas():

    def __init__(self, x, y, orientacao):
        self.x = x
        self.y = y
        self.orient = orientacao

    def setCoordenada(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setOr(self, orientacao):
        self.orient = orientacao

    def getOr(self):
        return self.orient

    def toString(self):
        return "({},{},{})".format(self.x, self.y, self.orient)

    def __lt__(self, other):
        a = (self.x ** 2 + self.y ** 2) ** (1/2)
        b = (other.x ** 2 + other.y ** 2) ** (1/2)
        return a < b



