import Pyro4

@Pyro4.expose
class SrCom:

    #
    #Receber Robo como parametro
    #
    def __init__(self, dados):
        self.dados = dados
    #   self.robo = robo


    def setID(self, valor):
        #self.robo.getID()
        pass

    def getPosInicial(self):
        return self.dados.getCoordenadas().toString()

    def getSituacaoMapa(self):
        pass

    def setMover(self, direcao):
        self.dados.coordenadas.setX(self.dados.getCoordenadas.getX() + 1)

    def setTime(self):
        # Trocar a cor do LED robo
        pass