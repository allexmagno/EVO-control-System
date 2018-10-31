import pika
from ssConnect import *
from manual import *
from srCom import *
import threading
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 62255))

host = ''
while host == '':
    host = server.recvfrom(1024)
port = 61030

clienteSS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clienteSS.connect((host[0].decode(),port))


msg = input("digite a mensagem: ")

####
# ...
####
if (msg == "getid"):
    clienteSS.send(msg.encode())
    print(clienteSS.recv(1024).decode())

elif (msg == "auto"):
    pass

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
            print(srcom.setMover("Frente"))
        elif(x == "a"):
            srcom.setMover("Esquerda")
        elif(x == "s"):
            srcom.setMover("Tras")
        elif(x == "d"):
            srcom.setMover("Direita")
        elif(x == "(espaço)"):
            pass
        elif(x == "(c)"):
            print(srcom.getPosInicial())


elif (msg == "whatever"):
    pass
####
# ...
####




'''
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 61030))
print("Server up", socket.gethostbyname(socket.gethostname()))

mensagem = server.recvfrom(1024)

robo = mensagem[1]

server.sendto("uri".encode(), robo)
mensagem =server.recvfrom(1024)

uri = mensagem[0].decode()
manual = Manual()
print(uri)
srcom = SRcom(uri)

x = ''
while x != "x":
    x = manual.controle()
    print(srcom.getPosInicial())
'''