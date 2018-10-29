from dados import *
from com import *
#from robo import *
import socket

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