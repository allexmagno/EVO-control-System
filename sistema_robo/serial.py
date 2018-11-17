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
    def deserializa(self, string):
        i = 0
        lista = []
        coords = string.split("/")
        while i < len(coords):
            lista.append(coords[i][0])
            lista.append(coords[i][1])

            i += 1

        return lista