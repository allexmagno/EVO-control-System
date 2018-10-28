import Pyro4.core
from sistema_robo.ssCom import *
from threading import Thread
class Com(Thread):
    def __init__(self, dados):
        Thread.__init__(self)
        sscom = SSCom(dados)
        self.deamon = Pyro4.Daemon()
        self.uri = self.deamon.register(sscom)


    def run(self):
        self.deamon.requestLoop()

    def getURI(self):
        return self.uri