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
        print("SSCOM")
        self.com.enviar("destino|" + str(destino.getX()) + str(destino.getY()), self.host)

    def setValidar(self):
        print("Enviando coordenadas")
        self.com.enviar("validar|" + str(self.dados.getCoordenadas().getX())+str(self.dados.getCoordenadas().getY()),
                        self.host)

        '''
        resposta = self.com.receber()
        msg = resposta[0].decode().split("|")
        if msg[0] == "validada":
            listaAtual = msg[1]

            # Desserializar lista
            listaDesserealizada = serial.desserializa(listaAtual)
            self.dados.setListaDeCacas(listaDesserealizada)
            return True

            #coordenadaAdv = msg2[2]
        elif msg[0] == "naoValidada":
            listaAtual = msg[1]

            # Desserializar lista
            listaDesserealizada = serial.desserializa(listaAtual)
            self.dados.setListaDeCacas(listaDesserealizada)
            return False

        elif msg[0] == "pausa":
            return "jogo pausado"
        elif msg[0] == "fimdejogo":
            return "fim de Jogo"
        else:
            print("Mensagem não Esperada")
        '''

    def getLista(self):
        return self.dados.getListaDeCacas()
