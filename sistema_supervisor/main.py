from manual import *
from autonomo import *
from com import *
from distributor import *
from switch import *
import compartilhados
from sacomTX import *
from sacomRX import *
from copy import deepcopy
import manualComp
from mensagens import *
import threading

def manualComunicacao():
    while True:
        manualComp.main_event.wait()

        with manualComp.main_lock:
            v = deepcopy(manualComp.main_msg)
            compartilhados.sw_msg = deepcopy({'_dir': 'ss', 'cmd': SS_to_SS.ValidaCaca,
                                              'x': v['x'], 'y': v['y']})
            compartilhados.sw_event.set()

        manualComp.main_event.clear()


robo = input("informe o nome do robo: ")
distributor = Distributor(robo)


switch = Switch(distributor)
switch.start()


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

            manualComp.init()
            manual = Manual(msg['uri'])
            manual.start()
            a = threading.Thread(target=manualComunicacao)
            a.start()

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

        elif msg['cmd'] == SS_to_SS.ValidaCaca_resp:

            with manualComp.lock_man:
                manualComp.msg_man = {'caca': msg['caca']}
                manualComp.event_man.set()

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