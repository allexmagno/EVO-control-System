import threading
from coordenadas import *

class SSCom:
    def __init__(self, com, host, dados):
        self.com = com
        self.dados = dados
        self.host = host

    def setPosAtual(self,posAtual):
        self.com.enviar("posAtual|" + posAtual.toString(), self.host)

    def getPosAtual(self):
        self.dados.coordenadas.toString()
        print(self.dados.coordenadas.toString())


    def setDestino(self,destino):
        self.com.enviar("destino|" + destino.toString(),self.host)

    def setValidar(self, x, y):
        coordenada = "(" + str(x) + "," + str(y) + ")"
        self.com.enviar("validar|" + coordenada,self.host)
        caca = self.com.receber()
        if(caca[0] == "ok"):
            self.dados.setcaca(coordenada)
            return caca[0]
        else:
            return "invalida"
