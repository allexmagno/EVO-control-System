from coordenadas import *
from estrategia import *


class Dados:

    def __init__(self, coordenadas, lista):
        self.coordenadas = Coordenadas(coordenadas)
        self.lista = lista
        self.estrategia = Estrategia(lista)
        self.listaEncontrada = []

    def getCoordenadas(self):
        return self.coordenadas

    def setDestino(self, coordenada):
        return True

    def setCoordenadas(self, x, y):
        self.coordenadas.setCoordenada(x, y)

    def getEstrategia(self, coordenada):
        return self.estrategia.getEstrategia(coordenada)


    def setListaDeCacas(self, lista):
        self.lista = lista
        self.estrategia.atualizaLista(lista)

    def getListaDeCacas(self):
        return self.lista

    def getDestino(self):
        pass

    def setEncontrada(self,encontrada):
        self.listaEncontrada.append(Coordenadas(encontrada))