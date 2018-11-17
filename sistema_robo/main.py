from dados import *
from com import *
from serial import *
#from robo import *
from broadcast import *
from ssCom import *
import time
import time
import socket
import threading
import subprocess

porta = 62255
comSS = Com(porta)

comSS.broadcast("SRequipe1", 65000)
msg = comSS.receber()


coord = comSS.receber()
hostSS = coord[1]

ipRobo = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
print(ipRobo)

#Divulga IP do robo por broadcast#
#Caso perca a conexão com o SS voltar a mandar broadcast

resposta = comSS.receber()
#print(resposta)
resposta = resposta[0].decode().split(",")

if(resposta[0] == "getid"):
    ##Enviar MAC do robo
    comSS.enviar("15",hostSS)

elif(resposta[0] == "auto"):
    comSS.enviar("ready",hostSS)
    resp = comSS.receber()

    print(resp[0].decode())

    split = resp[0].decode().split('|')
    print(split)

    i = 0

    cordInicial = []
    listCord = []

    while(i < len(split)):
        if(split[i] == "cord"):
            i += 1
            cordInicial.append(split[i][0])
            cordInicial.append(split[i][1])
        elif(split[i] == "lista"):
            i += 1
            cordenadas = split[i].split("/")
            print(cordenadas)
            j = 0
            while j < len(cordenadas):
                if (j == len(cordenadas)):
                    break
                else:
                    cordLista = []
                    cordLista.append(cordenadas[j][0])
                    cordLista.append(cordenadas[j][1])
                    listCord.append(cordLista)
                    j += 1
        i += 1

    print(cordInicial)
    print(listCord)

    ## Cord Inicial e Lista recebida
    #Chamar estrategia e comunicar com SS pela porta especifica

    dado = Dados(cordInicial,listCord)
    print(hostSS)
    robo = Robo(dado)

    ssCom = SSCom(comSS, hostSS, dado)
    ##Thread ssCOM para enviar mensagem
    #
    #

    # Desserializar lista
    serial = Serial()

    msgSS = ("","")
    while msgSS == ("",""):
        robo.setAutonomo(ssCom)
        msgSS = comSS.receber()
        msg = msgSS[0].decode().split("|")
        if(msg[0] == "confirmaMov"):
            listaAtual = msg2[1]
            listaDesserealizada = serial.desserializa(listaAtual)
            dado.getListaDeCacas(listaDesserealizada)
            robo.atualizaLista(listaDesserealizada)

            # Desserializar lista
            coordenadaAdv = msg2[3]

            msgSS2 = comSS.receber()
            msg2 = msgSS[0].decode().split("|")
            if msg2[0] == "mapa":
                listaAtual = msg2[1]

                # Desserializar lista
                listaDesserealizada = serial.desserializa(listaAtual)
                dado.getListaDeCacas(listaDesserealizada)
                robo.atualizaLista(listaDesserealizada)

                coordenadaAdv = msg2[3]
        elif msg[0] == "mapa":
                listaAtual = msg[1]

                #Desserializar lista
                listaDesserealizada = serial.desserializa(listaAtual)
                dado.getListaDeCacas(listaDesserealizada)
                robo.atualizaLista(listaDesserealizada)

                coordenadaAdv = msg[3]
        elif msg[0] == "validada":
            listaAtual = msg2[1]

            # Desserializar lista
            listaDesserealizada = serial.desserializa(listaAtual)
            dado.getListaDeCacas(listaDesserealizada)
            robo.atualizaLista(listaDesserealizada)

            coordenadaAdv = msg2[3]
        elif msg[0] == "naoValidada":
            listaAtual = msg2[1]

            # Desserializar lista
            listaDesserealizada = serial.desserializa(listaAtual)
            dado.getListaDeCacas(listaDesserealizada)
            robo.atualizaLista(listaDesserealizada)

            coordenadaAdv = msg2[3]
        elif msg[0] == "paradaEmergencia":
            break
        msgSS = ("","")

    '''
    aut = Autonomo(robo,dado)
    aut.inicia()
    '''
elif(resposta[0] == "manual"):


    #Começar Pyro#
    lista = []
    dados = Dados(coord[0], lista)
    # robo = Robo(dados)

    comSS.rpc(dados,robo)
    uri = com.getURI()

    comSS.enviar(str(uri),hostSS)
    comSS.start()

    sscom = SSCom(comSS, hostSS, dados)