from movimento import *
from coordenadas import *

class Autonomo:
    def __init__(self, coordAtual, coordInicial, coordAdv, sequencia, robo):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv
        self.mover = robo

    def setCoordenada(self, coordenada):
        self.coordAtual = coordenada

    def getCoordenada(self):
        return self.coordAtual.toString()

    def getAversario(self, adv):
        self.coordAdv = adv

    def getSeqAtualizada(self):
        return self.sequencia

    def setValidar(self):
        return self.coordAtual.toString()

    def executar(self):
        while self.sequencia != 0:

            self.sequencia.sort()
            i = 0
            while i in range(len(self.sequencia)):
                mx = self.sequencia(0).getX - self.coordAtual.getX
                my = self.sequencia(0).getY - self.coordAtual.getY

    # caso (x+, y+)
    def setNordeste(self, x, y, nav):
        if nav == 2:
            if self.coordAtual.getOr() == 'N':
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setRetornar()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setEsquerda()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setDireita()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if x > 0:
                self.mover.setDireita()
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                x = x - 1
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

        if nav == 1:
            if self.coordAtual.getOr() == 'L':
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setRetornar()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setEsquerda()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setDireita()
                x = x - 1
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if y > 0:
                self.mover.setEsquerda()
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                y = y - 1
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)


    # Caso (x+,y-)
    def setSudeste(self, x, y, orientacao, nav):
        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                # self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            # self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                # self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'O' and nav == 1:
            # self.mover.Retornar()
            x = x - 1
            self.coordAtual.setOr('L')
            while x > 0:
                # self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            # self.mover.setDireita()
            self.coordAtual.setOr('L')
            y = y + 1
            while y < 0:
                # self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                # self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            # self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                # self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                # ver.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            # self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                # self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

    # Caso (x-, y+)
    def setSudeste(self, x, y, orientacao):
        pass

    # Caso (x-, y-)
    def setSudoeste(self, x, y, orientacao):
        pass
