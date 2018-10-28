from sistema_robo.coordenadas import *
from sistema_robo.estrategia import *

class Dados:

    def __init__(self, coordenadas, lista):
        self.coordenadas = Coordenadas(coordenadas)
        self.estrategia = Estrategia(lista)

    def getCoordenadas(self):
        return self.coordenadas


    def setDestino(self):
        pass

    def setCoordenadas(self, x, y):
        self.coordenadas.setCoordenada(x, y)

    def getEstrategia(self):
        pass

