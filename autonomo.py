from movimento import *
from coordenadas import *


class Autonomo:

    def __init__(self, coordAtual, coordInicial, coordAdv,sequencia):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv

    def setCoordenada(self, coordenada):
        self.coordAtual = coordenada

    def getAversario(self, adv):
        self.coordAdv = adv

    def executar(self):
        pass