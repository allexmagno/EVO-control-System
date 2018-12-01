from coordenadas import *

class Serial:
    def __init__(self):
        pass

    def serializa(self, lista):
        i = 0
        serial = ""
        while i < len(lista):
            if(i == 0):
                serial = serial + str(lista[i][0]) + str(lista[i][1])
            else:
                serial = serial + "/" + str(lista[i][0]) + str(lista[i][1])
            i += 1
        return serial

    def desserializa(self, string):
        i = 0
        lista = []
        coords = string.split("/")
        while i < len(coords):
            coorde = Coordenadas((coords[i][0], coords[i][1]))
            lista.append(coorde)
            i += 1

        return lista