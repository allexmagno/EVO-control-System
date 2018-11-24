from dados import *
from math import sqrt

class Estrategia:

    def __init__(self, lista):
        self.lista = lista

    def getEstrategia(self, coordenadas):
        self.ordenaSequenciaCaca(coordenadas)
        return self.lista[0]

    def ordenaSequenciaCaca(self,coordenadas):
        i = 0
        j = 0

        listaDeCacas = self.lista
        x_atual = coordenadas.getX()
        y_atual = coordenadas.getY()

        auxDistancia = sqrt(((int(self.lista[0].getX()) - x_atual) ** 2) + ((int(self.lista[0].getY()) - y_atual) ** 2))

        while i < (len(listaDeCacas)):

            if auxDistancia > sqrt(((int(self.lista[i].getX()) - x_atual) ** 2) + ((int(self.lista[i].getY()) - y_atual) ** 2)):
                auxDistancia = sqrt(((int(self.lista[i].getX()) - x_atual) ** 2) + ((int(self.lista[i].getY()) - y_atual) ** 2))
                j = i
            i = i + 1


        self.lista = listaDeCacas


    def setEstrategia(self, lista):
        i = 0
        j = 0

        x_atual = self.coordAtual.getX()
        y_atual = self.coordAtual.getY()

        aux = (((self.sequencia[0].getX() - x_atual) ** 2) + (self.sequencia[0].getY() - y_atual) ** 2) ** (1 / 2)
        while i < (len(self.sequencia)):

            if aux > (((self.sequencia[i].getX() - x_atual) ** 2) + (self.sequencia[i].getY() - y_atual) ** 2) ** (
                    1 / 2):
                aux = (((self.sequencia[i].getX() - x_atual) ** 2) + (self.sequencia[i].getY() - y_atual) ** 2) ** (
                        1 / 2)
                j = i
            i = i + 1

        x = self.sequencia[j].getX() - self.nav.getCoord().getX()
        y = self.sequencia[j].getY() - self.nav.getCoord().getY()

        print(x)
        print(y)
        if (x > 0 and y > 0):
            print("Ne")
            self.nav.setNe(x, y, 1)
        if (x > 0 and y < 0):
            print("Se")
            self.nav.setSe(x, y, 1)
        if (x < 0 and y > 0):
            print("No")
            self.nav.setNo(x, y, 1)
        if (x < 0 and y < 0):
            print("So")
            self.nav.setSo(x, y, 1)
        if (x == 0):
            if (y > 0):
                print("N")
                self.nav.setNe(x, y, 1)
            if (y < 0):
                print("S")
                self.nav.setSe(x, y, 1)
        if (y == 0):
            if (x > 0):
                print("L")
                self.nav.setNe(x, y, 1)
            if (x < 0):
                print("O")
                self.nav.setSo(x, y, 1)
        print("caca aqui " + self.sequencia[j].toString())
        del self.sequencia[j]

        self.coordAtual = self.nav.getCoord()

    def atualizaLista(self, lista):
        self.lista = lista

