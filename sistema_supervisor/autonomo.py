import threading
import socket
import subprocess
from broadcast import *


class Autonomo:

    def __init__(self, coordInicial, lista):
        self.coordInicial = coordInicial
        self.lista = lista

    def inicia(self):
        ipSS = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
        print(ipSS)

        divulgaIP = Broadcast()
        divulgaIP.cast(ipSS)

        host = '0.0.0.0'
        # Porta para o Robo mandar as instruções do modo autonomo#
        port = 63030

        serverSS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSS.bind((host, port))

        serverSS.listen(10)

        print("Ouvindo... porta " + str(port))

        def clienteSS(cliente_socket):
            resposta = cliente_socket.recv(1024)

            split = resposta.split('|')
            i = 0

            if(split[i] == "destino"):
                ##Informar ao SA proximo destino do robo
                ##Encaminhar ao robo situação atualizada do MAPA posição adversario e lista de caças()
                pass
            elif(split[i] == "encontrada"):
                ##Solicitar validação do SA para a caça
                ##Confirmar ou nao validação e enviar situação do Mapa atualizada
                pass
            elif(split[i] == "..."):
                pass

        while (True):
            client, addr = serverSS.accept()
            cliente = threading.Thread(target=clienteSS, args=(client,))
            cliente.start()


    def autonomo(self, view):
        print(view)

    def setLista(self):
        pass
