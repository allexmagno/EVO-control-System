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
        while msgSR == ("",""):
            msgSR = self.com.receber()
            msg = msgSR[0].decode().split("|")
            if msg[0] == "destino":
                serial = Serial()
                ##Encaminhar para SA destino

                #Nova Lista recebida pelo SA
                novaLista = []
                self.lista = novaLista
                listaSerializada = serial.serializa(novaLista)

                coordAdv = (6,6)

                resp = "confirmaMov|" + coordAdv[0] + coordAdv[1] + "|" + listaSerializada
                self.com.enviar(msgSR[1],resp)


            elif msg[0] == "validar":
                pass
            msgSR = ("", "")

    def autonomo(self, view):
        print(view)

    def setLista(self):
        pass
