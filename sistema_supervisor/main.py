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


com = Com(65500)


host = com.descoberta("SRequipe1")

coord = input("Coordenada inicial do Robo: ")
com.enviar(coord)
uri = com.receber()
srcom = SRCom(uri[0])
manual = Manual()


comando = ''
while comando != "x":
   comando = manual.controle()

   if comando == "w":
       srcom.setMover("frente")

   elif comando == "c":
       scrom.getPosAtual()



'''
discovery = Discovery()

ipRobo = discovery.encontraIP()
port = 61030

clienteSS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clienteSS.connect((ipRobo[0].decode(),port))

## Receber informação do SA
# STUB :
msg = input("digite a mensagem: ")

if (msg == "getid"):
    clienteSS.send(msg.encode())
    print(clienteSS.recv(1024).decode())

elif (msg == "auto"):
    estadoRobo = ""

    while(estadoRobo != "ready"):
        clienteSS.send(msg.encode())
        estadoRobo = clienteSS.recv(1024)
        estadoRobo = estadoRobo.decode()

    ## Receber do SA Cordenada Inicial e Lista de caças
    #STUB:
    Lista = []
    cordI = [0,0]
    cord0 = [3, 2]
    cord1 = [6, 1]
    cord2 = [5, 5]

    Lista.append(cord0)
    Lista.append(cord1)
    Lista.append(cord2)

    #serializar dados e encaminhar ao SR
    serializa = Serial()
    strSerial = serializa.serializa(Lista)

    #Classe "Autonomo" irá tratar do recebimento das mensagens do SR e transmitirá ao SA
    aut = Autonomo(cordI,Lista)

    inicio = "cord|" + str(cordI[0]) + str(cordI[1]) + "|lista|" + strSerial

    #Envia cordenada Inicial e Lista de caças para o Robo
    clienteSS.send(inicio.encode())

    #Inicial autonomo para receber mensagens na porta especifica
    aut.inicia()

elif (msg == "manual"):
    clienteSS.send(msg.encode())
    uri = clienteSS.recv(1024).decode()

    print("Uri:" + uri)

    manual = Manual()
    srcom = SRcom(uri)

    x = ''
    while x != "x":
        x = manual.controle()
        if(x == "w"):
            print(srcom.setMover("frente"))
        elif(x == "a"):
            srcom.setMover("esquerda")
        elif(x == "s"):
            srcom.setMover("retornar")
        elif(x == "d"):
            srcom.setMover("direita")
        elif(x == "(espaço)"):
            pass
        elif(x == "(c)"):
            print(srcom.getPosInicial())


elif (msg == "whatever"):
    pass
'''