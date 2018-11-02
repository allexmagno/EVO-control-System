
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

