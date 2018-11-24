from threading import Thread
from srCom import *


class Manual(Thread):
    def __init__(self, uri):
        Thread.__init__(self)
        self.rpc = SRCom(uri)

    def run(self):

        while True:
            a =  input("(w) Frente\n"
                         "(s) Retornar\n"
                         "(d) Direirta\n"
                         "(a) Esquerda\n"
                         "(espaço) Caça\n"
                         "(c) Coordenadas\n")

            if a == 'w':
                self.rpc.setMover('frente')

            elif a == 's':
                self.rpc.setMover('retornar')

            elif a == 'a':
                self.rpc.setMover('esquerda')

            elif a == 'd':
                self.rpc.setMover('direita')
