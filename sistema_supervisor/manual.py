from threading import Thread
from srCom import *
import manualComp
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

                x = int(input("x atual: "))
                y = int(input("y atual: "))

                with manualComp.main_lock:
                    manualComp.main_msg = {'x': x, 'y': y}
                    manualComp.main_event.set()

                manualComp.event_man.wait()
                msg = deepcopy(manualComp.msg_man)

                if msg['caca'] == 1:
                    print("CAÇA VALIDADA PELO SA")

                elif msg['caca'] == 0:
                    print("CAÇA NÃO VALIDADA PELO SA")

                manualComp.event_man.clear()
