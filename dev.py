<<<<<<< HEAD
#from autonomo import *
from coordenadas import *
import subprocess

t = subprocess.check_call()
coord = Coordenadas(0,0,'N')
c1 = Coordenadas(4,1,'N')
c2 = Coordenadas(1,20,'N')
c3 = Coordenadas(14,51,'N')
c4 = Coordenadas(10,9,'N')
c5 = Coordenadas(7,1,'N')
c6 = Coordenadas(3,3,'N')
c7 = Coordenadas(1,5,'N')
c8 = Coordenadas(3,1,'N')

a = [1,2,3,4,5,2,23,342,5436,76,8,79,6]
#aut = Autonomo(coord,coord,coord,a)
b = [c1, c2, c3, c4, c5, c6, c7, c8]
i = 0
o = -9

o = abs(o)
print(o)
=======
import threading
from time import sleep


a = [1,1,2,3,4,4]
b = [2]
print(len(a), len(b))
del a[5]
del b[0]

if len(a) > 0:
    print(a)

if len(b) == 0:
    print(b)

>>>>>>> cc7772903736940fbd957847836f18a133a99c95
