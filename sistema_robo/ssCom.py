import threading


class SSCom:
    def __init__(self, com, host, dados):
        self.com = com
        self.dados = dados
        self.host = host

    def setPosAtual(self):
        pass

    def getPosAtual(self):
<<<<<<< HEAD
        self.dados.coordenadas.toString()
=======
        print(self.dados.coordenadas.toString())
>>>>>>> d5f10c6d2e49f7f627c040ef2cc882b1123f3877

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
