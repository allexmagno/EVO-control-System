from dados import *
from com import *
#from robo import *
import socket
import threading
import subprocess

print(subprocess.getoutput("hostname -I | cut -f1 -d \" \" "))
porta = 62255
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.sendto(subprocess.getoutput("hostname -I | cut -f1 -d \" \" ").encode(), ('255.255.255.255', porta))

host = '0.0.0.0'
port = 61030

serverSR = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSR.bind((host,port))

serverSR.listen(10)

print("Ouvindo... porta " + str(port))

def clienteSS(cliente_socket):
    resposta = cliente_socket.recv(1024)

    ####
    # ...
    ####
    if(resposta.decode() == "getid"):
        cliente_socket.send("15".encode())
        pass

    elif(resposta.decode() == "auto"):
        pass

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
    ####
    #...
    ####
    cliente_socket.close()

while(True):
    client, addr = serverSR.accept()
    cliente = threading.Thread(target=clienteSS, args= (client,))
    cliente.start()


'''

porta = 61030
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.sendto("robo".encode(), ('255.255.255.255', porta))
mensagem = client.recvfrom(1024)


lista = []
dados = Dados('(0,0)', lista)
#robo = Robo(dados)

comunicacao = Com(dados,  porta)
uri = comunicacao.getURI()

if mensagem[0].decode() == "uri":
    client.sendto(uri.enconde(), mensagem[1])

comunicacao.start()

t = ''
while t != "x":
    x = int(input("x = "))
    y = int(input("y = "))
    dados.setCoordenadas(x, y)
    t = input("atualizar?")
'''