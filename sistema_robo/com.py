import Pyro4.core
from srCom import *
from threading import Thread
import subprocess
import socket
import netifaces


@Pyro4.expose
class Com(Thread):
    def __init__(self, porta):
        Thread.__init__(self)
        self.ip = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
        print(self.ip)
        self.porta = porta
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', self.porta))
        self.uri = ''

        ##### LEMBRAR DE CONFERIR A INTERFACE
        self.mac = netifaces.ifaddresses('wlan1')[netifaces.AF_LINK]

    def rpc(self, dados, robo):
        self.srcom = SRCom(dados, robo)
        self.deamon = Pyro4.Daemon(host=self.ip, port=64000)
        self.uri = self.deamon.register(self.srcom)

    def run(self):
        self.deamon.requestLoop()

    def getURI(self):
        return self.uri

    def getMac(self):
        return self.mac

    def getIP(self):
        return self.ip

    def enviar(self, msg, host):
        self.client.sendto(msg.encode(), host)

    def receber(self):
        return self.client.recvfrom(1024)

    def broadcast(self, msg, porta):
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.client.sendto(msg.encode(), ('255.255.255.255', porta))
