

class quadrante():
    def __init__(self,quadranteInicial,sequencia):
        self.quadranteInicial = quadranteInicial
        self.sequencia = sequencia
        self.quadA = []
        self.quadB = []
        self.quadC = []
        self.quadIgnorado = []

    def dividirCacas(self):
        i = 0
        while i < len(self.sequencia):
            if(self.quadranteInicial == 0):
                if((self.sequencia[i].getX() <= 2 and self.sequencia[i].getY() <= 2) or (self.sequencia[i].getX() == 3 and self.sequencia[i].get3() == 3) ):
                    self.quadA[i] = self.sequencia[i]
                elif(self.sequencia[i].getX() >= 3 and self.sequencia[i].getY() <= 2):
                    if((self.sequencia[i].getX() == 5 and self.sequencia[i].getY() == 2) or (self.sequencia[i].getX() == 6 and self.sequencia[i].getY() == 2)):
                        self.quadIgnorado[i] = self.sequencia[i]
                    self.quadB[i] = self.sequencia[i]
                elif(self.sequencia[i].getX() <= 2 and self.sequencia[i].getY() >= 3):
                    if((self.sequencia[i].getX() == 2 and self.sequencia[i].getY() == 5) or (self.sequencia[i].getX() == 2 and self.sequencia[i].getY() == 6)):
                        self.quadIgnorado[i] = self.sequencia[i]
                    self.quadC[i] = self.sequencia[i]
                else:
                    self.quadIgnorado[i] = self.sequencia[i]

            if(self.quadranteInicial == 1):
                if((self.sequencia[i].getX() >= 4 and self.sequencia[i].getY() >= 4) or (self.sequencia[i].getX() == 3 and self.sequencia[i].get3() == 3) ):
                    self.quadA[i] = self.sequencia[i]
                elif(self.sequencia[i].getX() >= 4 and self.sequencia[i].getY() <= 3):
                    if((self.sequencia[i].getX() == 4 and self.sequencia[i].getY() == 0) or (self.sequencia[i].getX() == 4 and self.sequencia[i].getY() == 1)):
                        self.quadIgnorado[i] = self.sequencia[i]
                    self.quadB[i] = self.sequencia[i]
                elif(self.sequencia[i].getX() <= 3 and self.sequencia[i].getY() >= 4):
                    if((self.sequencia[i].getX() == 0 and self.sequencia[i].getY() == 4) or (self.sequencia[i].getX() == 1 and self.sequencia[i].getY() == 4)):
                        self.quadIgnorado[i] = self.sequencia[i]
                    self.quadC[i] = self.sequencia[i]
                else:
                    self.quadIgnorado[i] = self.sequencia[i]
            i = i + 1
