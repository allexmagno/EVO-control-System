import Pyro4
from robo import *

@Pyro4.expose
class SRCom:

    #
    #Receber Robo como parametro
    #
    def __init__(self, dados, robo):
        self.dados = dados
        self.robo = robo


    def setID(self, valor):
        self.robo.getID()
        pass

    def getPosInicial(self):
        return self.dados.getCoordenadas().toString()

    def getSituacaoMapa(self):
        pass

    def setMover(self, direcao):
        self.robo.setManual(direcao)

    def setTime(self):
        # Trocar a cor do LED robo
        pass