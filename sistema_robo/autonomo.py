from dados import *
from robo import *
from discoverySS import *
import socket

class Autonomo:

    def __init__(self,robo):
        self.robo = robo

    def inicia(self):
        discovery = Discovery()
        ipSS = discovery.encontraIP()
        port = 63030

        clienteSR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteSR.connect((ipSS[0].decode(), port))




    def encontraCaca(self):
        pass