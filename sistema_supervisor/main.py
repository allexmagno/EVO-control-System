import pika
from ssConnect import *
from manual import *
from srCom import *
import threading
import socket
from autonomo import *
from serial import *
from discoveryRobo import *
from com import *

clienteSS = Com(65000)
host = clienteSS.descoberta("SRequipe1")
print(host)
coord = input("Coordenada inicial do Robo: ")
clienteSS.enviar(host, coord)

## Receber informação do SA

##
#   Provavelmente terá uma Classe para comunicar com SA
#   Esta comunicação (com SA) será feito primeiro
#   Portanto o modo de jogo já estará decidido
##

msg = input("digite a mensagem: ")

if (msg == "getid"):
    clienteSS.enviar(host,msg)
    print(clienteSS.receber())

elif (msg == "auto"):
    estadoRobo = ""

    while (estadoRobo != "ready"):
        clienteSS.enviar(host,msg)
        estadoRobo = clienteSS.receber()
        estadoRobo = estadoRobo[0].decode()

    ## Receber do SA Cordenada Inicial e Lista de caças
    # STUB:
    Lista = []
    cordI = [0, 0]
    cord0 = [3, 2]
    cord1 = [6, 1]
    cord2 = [5, 5]

    Lista.append(cord0)
    Lista.append(cord1)
    Lista.append(cord2)

    # serializar dados e encaminhar ao SR
    serializa = Serial()
    strSerial = serializa.serializa(Lista)

    # Classe "Autonomo" irá tratar do recebimento das mensagens do SR e transmitirá ao SA
    aut = Autonomo(cordI, Lista, clienteSS)

    inicio = "cord|" + coord + "|lista|" + strSerial

    # Envia cordenada Inicial e Lista de caças para o Robo
    clienteSS.enviar(host,inicio)

    # Inicial autonomo para receber mensagens na porta especifica
    aut.inicia()

elif (msg == "manual"):
    msg = msg + ",00"
    clienteSS.enviar(host,msg)
    uri2 = clienteSS.receber()
    uri = uri2[0].decode()

    print("Uri:" + uri)

    manual = Manual()
    srcom = SRCom(uri)

    x = ''
    while x != "x":
        x = manual.controle()

        if (x == "w"):
            print(srcom.setMover("frente"))
        elif (x == "a"):
            srcom.setMover("esquerda")
        elif (x == "s"):
            srcom.setMover("retornar")
        elif (x == "d"):
            srcom.setMover("direita")
        elif x == "c":
            print(srcom.getPosAtual())


elif (msg == "whatever"):
    pass
