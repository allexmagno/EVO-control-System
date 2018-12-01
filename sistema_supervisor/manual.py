from threading import Thread
from srCom import *
import compartilhados
from copy import deepcopy
from mensagens import *


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
                         "(v) Validar Caça\n"
                         "(c) Coordenadas\n")

            if a == 'w':
                self.rpc.setMover('frente')

            elif a == 's':
                self.rpc.setMover('retornar')

            elif a == 'a':
                self.rpc.setMover('esquerda')

            elif a == 'd':
                self.rpc.setMover('direita')

            elif a == 'v':
                self.rpc.setValidar()

                #with manualComp.main_lock:
                #    manualComp.main_msg = {'x': x, 'y': y}
                #    manualComp.main_event.set()

                #compartilhados.event_man.wait()
                #print("VALIDANDO MANUAL")
                #msg = deepcopy(compartilhados.msg_man)

                #if msg['caca'] == 1:
                #    print("CAÇA VALIDADA PELO SA")

                #elif msg['caca'] == 0:
                #    print("CAÇA NÃO VALIDADA PELO SA")

                #   compartilhados.event_man.clear()
