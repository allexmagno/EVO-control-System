class Coordenadas():

    def __init__(self, coordenadas):
        self.x = int(coordenadas[0])
        self.y = int(coordenadas[1])
        self.orient = ''
        if self.x == 0 and self.y ==0:
            self.orient = "L"
        elif self.x == 6 and self.y ==6:
            self.orient = "O"


    def atualizarFrente (self):
        if self.orient == "L":
            self.x = self.x + 1
        elif self.orient == "O":
            self.x = self.x - 1
        elif self.orient == "N":
            self.y = self.y + 1
        elif self.orient == "S":
            self.y = self.y -1

    def atualizarRe (self):
        if self.orient == "L":
            self.x = self.x - 1
            self.orient = "O"
        elif self.orient == "O":
            self.x = self.x + 1
            self.orient = "L"
        elif self.orient == "N":

            self.y = self.y - 1
            self.orient = "S"
        elif self.orient == "S":
            self.y = self.y + 1
            self.orient = "N"

    def atualizarDireita(self):
        if self.orient == "L":
            self.y = self.y - 1
            self.orient = "S"
        elif self.orient == "O":
            self.y = self.y + 1
            self.orient = "N"
        elif self.orient == "N":
            self.x = self.x + 1
            self.orient = "L"
        elif self.orient == "S":
            self.x = self.x - 1
            self.orient = "O"

    def atualizarEsquerda(self):
        if self.orient == "L":
            self.y = self.y + 1
            self.orient = "N"
        elif self.orient == "O":
            self.y = self.y - 1
            self.orient = "S"
        elif self.orient == "N":
            self.x = self.x - 1
            self.orient = "O"
        elif self.orient == "S":
            self.x = self.x + 1
            self.orient = "L"


    def indoPFrente(self):
        if self.orient == "L":
            return self.x + 1, self.y
        elif self.orient == "O":
            return self.x - 1, self.y
        elif self.orient == "N":
            return self.x, self.y + 1
        elif self.orient == "S":
            return self.x, self.y -1

    def indoPtras (self):
        if self.orient == "L":
            return self.x - 1, self.y
        elif self.orient == "O":
            return self.x + 1, self.y
        elif self.orient == "N":
            return self.x, self.y - 1

        elif self.orient == "S":
            return self.x, self.y + 1

    def indoPDireita(self):
        if self.orient == "L":
            return self.x, self.y - 1
        elif self.orient == "O":
            return self.x, self.y + 1
        elif self.orient == "N":
            return self.x + 1, self.y
        elif self.orient == "S":
            return self.x - 1, self.y

    def indoPEsquerda(self):
        if self.orient == "L":
            return self.x, self.y + 1
        elif self.orient == "O":
            return self.x, self.y - 1
        elif self.orient == "N":
            return self.x - 1, self.y
        elif self.orient == "S":
            return self.x + 1, self.y

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