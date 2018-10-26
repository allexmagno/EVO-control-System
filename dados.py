from coordenadas import *
from estrategia import *

class Dados:

    def __init__(self, coordenadas, lista):
        self.coordenadas = Coordenadas(coordenadas)
        self.estrategia = Estrategia(lista)

    def getCoordenadas(self):
        return self.coordenadas


    def setDestino(self):
        pass

    def setCoordenadas(self):
        pass


    def getEstrategia(self):
        pass

