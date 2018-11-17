from movimento import *
from dados import *
from coordenadas import *

class Robo:

    def __init__(self, dados):
        self.dados = dados
        self.mover = Movimento('outA', 'outD', 200)


    def setManual(self,  comando):
        if comando == "direita":
            self.mover.setDireita()
            self.dados.getCoordenadas().atualizarDireita()
        elif comando == "esquerda":
            self.mover.setEsquerda()
            self.dados.getCoordenadas().atualizarEsquerda()
        elif comando == "frente":
            self.mover.setFrente()
            self.dados.getCoordenadas().atualizarFrente()
        elif comando == "parar":
            self.mover.setParar()
        elif comando == "retornar":
            self.mover.setRetornar()
            self.dados.getCoordenadas().atualizarRe()


    def setAutonomo(self, ssCom):
        coordProxima = self.dados.getEstrategia(self.dados.getCoordenadas())
        coordAtual = self.dados.getCoordenadas()

        if coordProxima.getX() - coordAtual.getX() > 0:

            if self.dados.setDestino(Coordenadas(dados.getCoordenadas().getX() + 1, dados.getCoordenadas().getY(), "")):
                if self.dados.getCoordenadas().getOr()=="L":
                    self.setManual("frente")
                if self.dados.getCoordenadas().getOr()=="O":
                    self.setManual("retornar")
                if self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("direita")
                if self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("esquerda")

        if coordProxima.getX() - coordAtual.getX() < 0:
            if self.dados.setDestino(Coordenadas(dados.getCoordenadas().getX() - 1, dados.getCoordenadas().getY(), "")):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("retornar")
                if self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("frente")
                if self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("esquerda")
                if self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("direita")

        if coordProxima.getY() - coordAtual.getY() < 0:
            if self.dados.setDestino(Coordenadas(dados.getCoordenadas().getX(), dados.getCoordenadas().getY() - 1, "")):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("direita")
                if self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("esquerda")
                if self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("retornar")
                if self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("frente")

        if coordProxima.getY() - coordAtual.getY() > 0:
            if self.dados.setDestino(Coordenadas(dados.getCoordenadas().getX(), dados.getCoordenadas().getY() + 1, "")):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("esquerda")
                if self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("direita")
                if self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("frente")
                if self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("retornar")



