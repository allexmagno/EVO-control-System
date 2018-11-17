from dados import *
from robo import *
from discoverySS import *
from ssCom import *
import socket

class Autonomo:

    def __init__(self,robo, dado):
        self.robo = robo
        self.dado = dado

    def inicia(self):
        discovery = Discovery()
        ipSS = discovery.encontraIP()
        port = 63030

        clienteSR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteSR.connect((ipSS[0].decode(), port))

        ##
        #Começar a tratar qual a proxima caça e proximo movimento

        destino = self.dados.getEstrategia()
        clienteSR.send("destino|" + destino.encode())
        self.robo.setAutonomo(destino)

    def encontraCaca(self):
        pass