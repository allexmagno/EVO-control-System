import threading


class SSCom:
    def __init__(self, com, host, dados):
        self.com = com
        self.dados = dados
        self.host = host

    def setPosAtual(self):
        pass

    def getPosAtual(self):
        print(self.dados.coordenadas.toString())

    def sedDestino(self):
        self.com.enviar(self.dados.getDestino().toString())

    def setValidar(self, x, y):
        coordenada = "(" + x + "," + y + ")"
        self.com.enviar(coordenada)
        caca = self.com.receber()
        if(caca[0] == "ok"):
            self.dados.setcaca(coordenada)
            return caca[0]
        else:
            return "invalida"
