import abc


class SRCom(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractclassmethod
    def getID(cls):
        pass

    @abc.abstractclassmethod
    def getPosInicial(cls):
        pass

    @abc.abstractclassmethod
    def getSituacaoMapa(cls):
        pass

    @abc.abstractclassmethod
    def setMover(cls, direcao):
        pass

    @abc.abstractclassmethod
    def setTime(cls):
        pass
