from autonomo import *


#robot = Movimento('outA', 'outD', 200)
robot = "a"
c1 = Coordenadas(1,2,'N')
c2 = Coordenadas(0,0,'L')
c3 = Coordenadas(6,6,'O')
s = []
aut = Autonomo(c1,c2,c3,s,robot)
print(aut.getCoordenada())
print(c1.toString())