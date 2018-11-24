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
        self.host = ''


    def reconectar(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', self.porta))

    def getIP(self):
        return self.ip

    def enviar(self, host, msg):
        self.client.sendto(msg.encode(), host)

    def rx(self):
        def receber_msg():

            while True:
                print("esperando mensagem")
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
        msg = self.receber_inicial()

        print("host econtrado")
        self.enviar(msg[1], "SSequipe1")
        return msg



if __name__ == '__main__':
    com = Com(60000)

    com.receber()