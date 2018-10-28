import Pyro4

@Pyro4.expose
class SSCom:

    def __init__(self, dados):
        self.dados = dados


    def setID(self, valor):
        pass

    def getPosInicial(self):
        return self.dados.getCoordenadas().toString()

    def getSituacaoMapa(self):
        pass

    def setMover(self, direcao):
        pass

    def setTime(self):
        pass