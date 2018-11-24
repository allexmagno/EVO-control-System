from threading import Thread, Event, Lock
from serial import *
import compartilhados
import json
from copy import deepcopy
from mensagens import *

class Autonomo(Thread):

    def __init__(self, dist):
        Thread.__init__(self)
        self.serial = Serial()
        self.distributor = dist


    def run(self):
        while True:

            compartilhados.autonomo_event.wait()
            print("autonomo")

            with compartilhados.autonomo_lock:
                print("lendo msg no autonomo")
                msg = deepcopy(compartilhados.autonomo_msg)
                msg = msg['cmd']
                if msg == SS_to_SS.MovendoPara:
                    x, y = self.distributor.getCoord()
                    print("Robo está se movimentando para: " + x + y)

                elif msg == SS_to_SS.ValidaCaca:
                    print("Robo solicita validaçao de caça: " + msg['x'] + msg['y'])
                elif msg == SS_to_SA.PosicaoAtual:
                    print("posicao atual do robo é " + msg['x'] + msg['y'])
                else:
                    pass

                # Continuar todas as opções
                compartilhados.autonomo_event.clear()