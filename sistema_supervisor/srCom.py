import Pyro4

class SRCom:

    def __init__(self, uri):
        self.comando = Pyro4.Proxy(uri)

    def setID(self, valor):
        pass

    def getPosAtual(self):
        return self.comando.getPosInicial()

    def getSituacaoMapa(self):
        pass

    def setMover(self, direcao):
        self.comando.setMover(direcao)

    def setTime(self):
        pass

    def setValidar(self):
        pass