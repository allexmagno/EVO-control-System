import Pyro4.core
from ssCom import *
from threading import Thread
import subprocess

class Com(Thread):
    def __init__(self, dados, porta):
        Thread.__init__(self)
        sscom = SSCom(dados)
        self.ip = subprocess.getoutput("hostname -I | cut -f1 -d \" \" ")
        self.deamon = Pyro4.Daemon(host=self.ip,port=porta)

        self.uri = self.deamon.register(sscom)

    def run(self):
        self.deamon.requestLoop()

    def getURI(self):
        return self.uri

    def getIP(self):
        return self.ip