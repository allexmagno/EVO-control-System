import threading
import socket
import subprocess
from serial import *
from broadcast import *
from serial import *


class Autonomo:

    def __init__(self, coordInicial, lista, com):
        self.coordInicial = coordInicial
        self.lista = lista
        self.com = com

    def inicia(self):
        msgSR = ("","")
        novaLista = []

        cord0 = [3, 2]
        cord1 = [3, 5]
        cord2 = [5, 5]

        novaLista.append(cord0)
        novaLista.append(cord1)
        novaLista.append(cord2)

        while msgSR == ("",""):
            msgSR = self.com.receber()
            msg = msgSR[0].decode().split("|")
            if msg[0] == "destino":
                serial = Serial()
                print("msg robo: " + msg[0] + msg[1])
                ##Encaminhar para SA destino

                #Nova Lista recebida pelo SA

                self.lista = novaLista
                listaSerializada = serial.serializa(novaLista)

                coordAdv = (6,6)

                resp = "confirmaMov|" + listaSerializada + "|" + str(coordAdv[0]) + str(coordAdv[1]) + "|"
                self.com.enviar(msgSR[1],resp)


            elif msg[0] == "validar":
                ## Tratar a mensagem e verificar com SA se a posição passada pelo SR existe uma caça
                ##Confirmar ao SR

                print("msg robo: " + msg[0] + msg[1])
                serial = Serial()
                ##Encaminhar para SA destino

                # Nova Lista recebida pelo SA

                i = 0
                x = input("validar posicao: ")
                if(x == "s"):
                    del novaLista[0]

                self.lista = novaLista
                listaSerializada = serial.serializa(novaLista)

                coordAdv = (6, 6)

                resp = "validada|" + listaSerializada + "|" + str(coordAdv[0]) + str(coordAdv[1])
                self.com.enviar(msgSR[1], resp)

            elif msg[0] == "posAtual":
                print("msg robo: " + msg[0] + msg[1])

                serial = Serial()
                ##Encaminhar para SA destino


                self.lista = novaLista
                listaSerializada = serial.serializa(novaLista)

                coordAdv = (6, 6)

                resp = "mapa|" + listaSerializada + "|" + str(coordAdv[0]) + str(coordAdv[1])
                self.com.enviar(msgSR[1], resp)
            msgSR = ("", "")

    def autonomo(self, view):
        print(view)

    def ComunicaSA(self):
        ##chamar alguma classe para comunicar com SA e receber a situação do mapa
        pass
