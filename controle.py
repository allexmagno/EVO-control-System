from autonomo import *

import threading

robot = Movimento('outA', 'outD', 200)

c1 = Coordenadas(0,0,'L')
c2 = Coordenadas(0,0,'L')
c3 = Coordenadas(6,6,'O')
s = []
aut = Autonomo(c1,c2,c3,s,robot)



while (True):
    a = input("(1) Manual \n(2) Autonomo:")
    if a == "1":
        print("selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Parar \n")
        op = input("digite uma opcao:")

        if op == "a":
            robot.setParar()
            robot.setEsquerda()

        if op == "d":
            robot.setParar()
            t1 = threading.Thread(target=robot.setDireita())

        if op == "w":
            t2 = threading.Thread(target=robot.setFrente())

        if op == "s":
            t3 = threading.Thread(robot.setRetornar())
    if a == "2":
        t1 = int(input("x"))
        t2 = int(input("y"))
        t3 = int(input("nav"))
        aut.setNordeste(t1,t2,t3)
        print(aut.getCoordenada())

