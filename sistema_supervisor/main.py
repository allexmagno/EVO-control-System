import pika
from ssConnect import *
from manual import *
from srCom import *
import threading
import socket


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
