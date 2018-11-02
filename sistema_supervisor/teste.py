Lista = []

cordI = [0,0]

serial = "cord|" + str(cordI[0]) + str(cordI[1]) + "|lista|"

coordenada0 = (5,2)
coordenada1 = (2,2)
coordenada2 = (1,2)
coordenada3 = (6,2)

Lista.append(coordenada0)
Lista.append(coordenada3)
Lista.append(coordenada1)
Lista.append(coordenada2)
"cord|" + str(cordI[0]) + str(cordI[1]) + "|lista"
i = 0
while i < len(Lista):
    if(i == 0):
        serial = serial + str(Lista[i][0]) + str(Lista[i][1])
    else:
        serial = serial + "/" + str(Lista[i][0]) + str(Lista[i][1])
    i += 1

print(serial)

#second = first[j].split('/')
