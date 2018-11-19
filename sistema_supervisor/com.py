import subprocess
import socket


class Com():
    def __init__(self, porta):
        self.ip = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
        self.porta = porta
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', self.porta))


    def getIP(self):
        return self.ip

    def enviar(self, host, msg):
        self.client.sendto(msg.encode(), host)

    def receber(self):
        return self.client.recvfrom(1024)

    def descoberta(self, ssID):
        print("procurando robo")
        msg = self.receber()
        print(msg)
        while msg[0].decode() != ssID:
            msg = self.receber()

        print("host econtrado")
        self.enviar(msg[1], "SSequipe1")
        return msg[1]
