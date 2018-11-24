import subprocess
import socket
from threading import Thread, Event
import compartilhados
from copy import deepcopy


class Com():
    def __init__(self, porta):
        self.ip = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
        self.porta = porta
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', self.porta))
        self.roboPorta = 0
        self.roboIP = ''


    def reconectar(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', self.porta))

    def getIP(self):
        return self.ip

    def enviar(self, host, msg):
        self.client.sendto(msg.encode(), host)

    def getRobo(self):

        return self.roboIP, self.roboPorta

    def rx(self):
        def receber_msg():

            while True:
                msg = self.client.recvfrom(1024)

                with compartilhados.sr_lock:
                    mensagem = {'_dir': 'sr', 'cmd': msg[0].decode()}
                    compartilhados.sw_msg = deepcopy(mensagem)
                    compartilhados.sw_event.set()
                    print(mensagem)



        a = Thread(target=receber_msg)
        a.start()
    def descoberta(self):
        print("procurando robo")
        msg = self.client.recvfrom(1024)

        print("Robo econtrado")
        self.enviar(msg[1], "SSequipe1")
        self.roboIP, self.roboPorta = msg[1]
        return msg[0].decode()