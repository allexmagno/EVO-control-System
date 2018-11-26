from movimento import *
from dados import *
from coordenadas import *
import globalsFlags


class Robo:

    def __init__(self, dados, sscom):
        self.dados = dados
        self.mover = Movimento('outA', 'outD', 200)
        self.ssCOM = sscom

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



    def setAutonomo(self):
        coordProxima = self.dados.getEstrategia(self.dados.getCoordenadas())
        coordAtual = self.dados.getCoordenadas()

        i = 0

        if coordProxima.getX() - coordAtual.getX() > 0:

            if self.dados.setDestino(Coordenadas((self.dados.getCoordenadas().getX() + 1, self.dados.getCoordenadas().getY()))):
                atual = Coordenadas((self.dados.getCoordenadas().getX() + 1, self.dados.getCoordenadas().getY()))
                self.ssCOM.setDestino(atual)
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
                atual = Coordenadas((self.dados.getCoordenadas().getX() - 1, self.dados.getCoordenadas().getY()))
                self.ssCOM.setDestino(atual)
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
                atual = Coordenadas((self.dados.getCoordenadas().getX(), self.dados.getCoordenadas().getY() - 1))
                self.ssCOM.setDestino(atual)
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
                atual = Coordenadas((self.dados.getCoordenadas().getX(), self.dados.getCoordenadas().getY() + 1))
                self.ssCOM.setDestino(atual)
                if self.dados.getCoordenadas().getOr() == "L":
                    self.setManual("esquerda")
                elif self.dados.getCoordenadas().getOr() == "O":
                    self.setManual("direita")
                elif self.dados.getCoordenadas().getOr() == "N":
                    self.setManual("frente")
                elif self.dados.getCoordenadas().getOr() == "S":
                    self.setManual("retornar")

        else:
            atual = Coordenadas((self.dados.getCoordenadas().getX(), self.dados.getCoordenadas().getY()))
            #Caso seja a posição de uma caça enviar um solicitação de validação
            #self.ssCOM.setValidar(coordProxima.getX(),coordProxima.getY())
            self.validarCaca()
            i = 1

            ## Nesse ponto o robo deve aguardar a resposta vinda do SA
            # SUGESTAO
            # criar um metodo que execute uma thread em com para receber as mensagens durante a execução do jogo
            # tanto para validacao das caças quanto pause e parada de emergencia
            # nesse metodo ele trata as mensagens e direciona para onde deve ir
            # O problema é conseguir deixar este método aguardando a resposta
            # Talvez possa usar um threading.Event.wait()

        # Passar a posiçao atual independente de ser uma caça ou nao
        if i == 0:
            self.ssCOM.setPosAtual(atual)
        i = 0

        #Confirmar se A posição está correta
    def atualizaLista(self,lista):
        self.dados.getListaDeCacas(lista)

    def validarCaca(self):

        x = self.dados.getCoordenadas().getX()
        y = self.dados.getCoordenadas().getY()

        self.ssCOM.setValidar(x, y)
        globalsFlags.com_event.set()

        globalsFlags.robo_event.wait()




        pass