from manual import *
from autonomo import *
from com import *
from distributor import *
from switch import *
import compartilhados
from sacomTX import *
from sacomRX import *
from copy import deepcopy
import threading




## Iniciar a comunicação com o Robo
#clienteSS = Com(65000)
#srHost = clienteSS.descoberta()
#host = srHost[1]

## Iniciar Classe compartilhada
robo = input("informe o nome do robo: ")
distributor = Distributor(robo)


switch = Switch(distributor)
switch.start()

## Iniciar a  comunicação vinda do SA
#hostSA = input("Informe o IP do SA: ")
#tx = SAcomTX('localhost')
#tx.start()

while True:

    compartilhados.main_event.wait()

    msg = deepcopy(compartilhados.main_msg)

    if 'modo' in msg:

        if msg['modo'] == 'auto':
            print("MODO AUTONOMO\n")
            print("Iniciando modo autonomo")
            auto = Autonomo(distributor)
            auto.start()

        elif msg['modo'] == 'manual':
            print("MODO MANUAL\n")
            manual = Manual(msg['uri'])
            manual.start()

        else:
            print("Modo invalido")

    elif 'cmd' in msg:

        if msg['cmd'] == 'pause':
            pass

        elif msg['cmd'] == 'continue':
            pass

        elif msg['cmd'] == 'fim':

            decisao = int(input("Fim de jogo \n O que deseja fazer? \n(1) novo jogo\n(2) encerrar\n"))

            if decisao == 1:
                pass
            elif decisao == 2:
                exit(-1)

            else:
                print("comando inválido")

    compartilhados.main_event.clear()

'''
msg = input("Modo de Jogo: ")
#compartilhados.switch_event.set()

if msg == 'manual':
    pass

elif msg == "auto":
    auto = Autonomo(clienteSS, distributor)
    auto.start()
'''