import threading
from coordenadas import *
from time import sleep

coord = Coordenadas(0,0,'N')
c1 = Coordenadas(4,1,'N')
c2 = Coordenadas(1,20,'N')
c3 = Coordenadas(1,1,'N')
c4 = Coordenadas(10,9,'N')
c5 = Coordenadas(7,1,'N')
c6 = Coordenadas(3,3,'N')
c7 = Coordenadas(1,5,'N')
c8 = Coordenadas(3,1,'N')


def mensagem():
    i = 0
    while i <= 5:
        print("thread ", i)
        i = i + 1
        sleep(1)

a = threading.Thread(target=mensagem)
b = threading.Thread(target=mensagem)
a.start()
b.start()
while a.isAlive():
    a.join()
    print("a")