import threading
from coordenadas import *



class SSCom:
    def __init__(self, com, host, dados):
        self.com = com
        self.dados = dados
        self.host = host

    def setPosAtual(self,posAtual):
        self.com.enviar("posAtual|" + str(posAtual.getX()) + str(posAtual.getY()), self.host)

    def getPosAtual(self):
        self.dados.coordenadas.toString()
        print(self.dados.coordenadas.toString())


    def setDestino(self,destino):
        self.com.enviar("destino|" + str(destino.getX()) + str(destino.getY()),self.host)

    def setValidar(self, x, y):
        self.com.enviar("validar|" + str(x) + str(y),self.host)
