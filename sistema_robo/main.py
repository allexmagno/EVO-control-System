from dados import *
from com import *
from robo import *
from broadcast import *
from ssCom import *
import time
import time
import socket
import threading
import subprocess

porta = 62255
com = Com(porta)


### todos os processos iniciais da partida

com.broadcast("SRequipe1", 65000)
msg = com.receber()


coord = com.receber()
lista = []
dados = Dados(coord[0].decode(), lista)
robo = Robo(dados)

com.rpc(dados, robo)
host = coord[1]
print(str(com.getURI()))

com.enviar(str(com.getURI()), host)
com.start()

sscom = SSCom(com, host, dados)


# simulando o robo movimentando

while(True):
    comando = input("(a) validar\n"
                    "(s) posicao\n")

    if comando == "a":
        x = input("valor de x = ")
        y = input("valor de y = ")
        sscom.setValidar(x,y)

    elif comando == "s":
        sscom.getPosAtual()



'''
ipRobo = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
print(ipRobo)

#Divulga IP do robo por broadcast#
#Caso perca a conexão com o SS voltar a mandar broadcast
divulgaIP = Broadcast()
divulgaIP.cast(ipRobo)

host = '0.0.0.0'
port = 61030

serverSR = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSR.bind((host,port))

serverSR.listen(10)

print("Ouvindo... porta " + str(port))

def clienteSS(cliente_socket):
    resposta = cliente_socket.recv(1024)

    if(resposta.decode() == "getid"):
        ##Enviar MAC do robo
        cliente_socket.send("15".encode())

    elif(resposta.decode() == "auto"):
        cliente_socket.send("ready".encode())
        resp = cliente_socket.recv(1024)

        print(resp.decode())

        split = resp.decode().split('|')
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
        robo = Robo(dado)

        aut = Autonomo(robo)
        aut.inicia()

    elif(resposta.decode() == "manual"):
        porta = 61031

        #Começar Pyro#
        lista = []
        dados = Dados('(0,0)', lista)
        # robo = Robo(dados)

        comunicacao = Com(dados, porta)
        uri = comunicacao.getURI()

        cliente_socket.send(str(uri).encode())
        comunicacao.start()

    elif(resposta.decode() == "whatever"):
        pass

    cliente_socket.close()

while(True):
    client, addr = serverSR.accept()
    cliente = threading.Thread(target=clienteSS, args= (client,))
    cliente.start()
'''