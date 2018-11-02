class Coordenadas():

    def __init__(self, x, y, orientacao):
        self.x = x
        self.y = y
        self.orient = orientacao

    def __init__(self, coordenadas):
        self.x = coordenadas[0]
        self.y= coordenadas[1]
        self.orient = " "
        if self.x == 0 and self.y ==0:
            self.orient = "L"
        elif self.x == 6 and self.y ==6:
            self.orient = "O"


    def atualizarFrente (self):
        if self.orient == "L":
            self.x = self.x + 1
        if self.orient == "O":
            self.x = self.x - 1
        if self.orient == "N":
            self.y = self.y + 1
        if self.orient == "S":
            self.y = self.y -1

    def atualizarRe (self):
        if self.orient == "L":
            self.x = self.x - 1
            self.orient = "O"
        if self.orient == "O":
            self.x = self.x + 1
            self.orient = "L"
        if self.orient == "N":
            self.y = self.y + 1
            self.orient = "S"
        if self.orient == "S":
            self.y = self.y -1
            self.orient = "N"

    def atualizarDireita(self):
        if self.orient == "L":
            self.y = self.y - 1
            self.orient = "S"
        if self.orient == "O":
            self.y = self.y + 1
            self.orient = "N"
        if self.orient == "N":
            self.x = self.x + 1
            self.orient = "L"
        if self.orient == "S":
            self.x = self.x - 1
            self.orient = "O"

    def atualizarEsquerda(self):
        if self.orient == "L":
            self.y = self.y + 1
            self.orient = "N"
        if self.orient == "O":
            self.y = self.y - 1
            self.orient = "S"
        if self.orient == "N":
            self.x = self.x - 1
            self.orient = "O"
        if self.orient == "S":
            self.x = self.x + 1
            self.orient = "L"

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



