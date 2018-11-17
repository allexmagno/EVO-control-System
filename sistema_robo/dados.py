from coordenadas import *
from estrategia import *


class Dados:

    def __init__(self, coordenadas, lista):
        self.coordenadas = Coordenadas(coordenadas)
        self.estrategia = Estrategia(lista)

    def getCoordenadas(self):
        return self.coordenadas


    def setDestino(self, coordenada):
        return True

    def setCoordenadas(self, x, y):
        self.coordenadas.setCoordenada(x, y)

    def getEstrategia(self):
        pass

    def getDestino(self):
        pass

    def getListaDeCacas(self, lista):
        self.estrategia.atualizaLista(lista)




