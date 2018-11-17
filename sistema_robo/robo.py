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


    def setAutonomo(self,ssCOM):
        coordProxima = self.dados.getEstrategia(self.dados.getCoordenadas())
        ssCOM.setDestino(coordProxima)
        coordAtual = self.dados.getCoordenadas()


        if coordProxima.getX() - coordAtual.getX() > 0:

            if self.dados.setDestino(Coordenadas((self.dados.getCoordenadas().getX() + 1, self.dados.getCoordenadas().getY()))):
                if self.dados.getCoordenadas().getOr()=="L":
                    self.setManual("frente")
                elif self.dados.getCoordenadas().getOr()=="O":
                    self.setManual("retornar")
                elif self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("direita")
                elif self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("esquerda")

        elif coordProxima.getX() - coordAtual.getX() < 0:
            if self.dados.setDestino(Coordenadas((self.dados.getCoordenadas().getX() - 1, self.dados.getCoordenadas().getY()))):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("retornar")
                elif self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("frente")
                elif self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("esquerda")
                elif self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("direita")

        elif coordProxima.getY() - coordAtual.getY() < 0:
            if self.dados.setDestino(Coordenadas((self.dados.getCoordenadas().getX(), self.dados.getCoordenadas().getY() - 1))):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("direita")
                elif self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("esquerda")
                elif self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("retornar")
                elif self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("frente")

        elif coordProxima.getY() - coordAtual.getY() > 0:
            if self.dados.setDestino(Coordenadas((self.dados.getCoordenadas().getX(), self.dados.getCoordenadas().getY() + 1))):
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("esquerda")
                elif self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("direita")
                elif self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("frente")
                elif self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("retornar")

        else:
            #Caso seja a posição de uma caça enviar um solicitação de validação
            situacao = ssCOM.setValidar(coordProxima.getX(),coordProxima.getY())
            if situacao == "ok":
                pass
            elif situacao == "invalida":
                pass

        # Passar a posiçao atual independente de ser uma caça ou nao
        ssCOM.setPosAtual(coordProxima)

        #Confirmar se A posição está correta
    def atualizaLista(self,lista):
        self.dados.getListaDeCacas(lista)