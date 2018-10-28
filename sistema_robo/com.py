import Pyro4.core
from ssCom import *
from threading import Thread
class Com(Thread):
    def __init__(self, dados):
        Thread.__init__(self)
        sscom = SSCom(dados)
        self.deamon = Pyro4.Daemon(host = "192.168.15.110",port= 6896)

        self.uri = self.deamon.register(sscom)

        ns = Pyro4.locateNS(host = "192.168.15.110",port= 6895, broadcast= True, hmac_key= None)

        ns.register('obj',self.uri)
        Pyro4.Daemon.startNSloop()

    def run(self):
        self.deamon.requestLoop()

    def getURI(self):
        return self.uri