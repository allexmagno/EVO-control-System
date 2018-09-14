from autonomo import *
import threading

robot = Movimento('outA', 'outD', 200)

c1 = Coordenadas(0, 0, 'L')
c2 = Coordenadas(0, 0, 'L')
c3 = Coordenadas(6, 6, 'O')
s = []

aut = Autonomo(c1, c2, c3, s, robot)


def setAutonomo():
    s = int(input("1 (Ne), 2 (Se), 3 (No), 4 (Ne)"))
    t1 = int(input("x: "))
    t2 = int(input("y: "))
    t3 = int(input("nav: "))

    if s == 1:
        aut.setNe(t1, t2, t3)
    elif s == 2:
        aut.setNe(t1, t2, t3)
    elif s == 3:
        aut.setNe(t1, t2, t3)
    elif s == 4:
        aut.setNe(t1, t2, t3)

    print(aut.getCoordenada())


def setManual():
    print(
        "selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Retornar \n space - Parar \n")
    op = input("digite uma opcao:")

    if op == "a":
        a =threading.Thread(target=robot.setEsquerda)
        a.start()

    if op == "d":
        d = threading.Thread(target=robot.setDireita)
        d.start()
    if op == "w":
        w = threading.Thread(target=robot.setFrente)
        w.start()

    if op == "s":
        s = threading.Thread(target=robot.setRetornar)
        s.start()

    if op == chr(32):
        spc = threading.Thread(target=robot.setParar)
        spc.start()


while (True):
    a = input("(1) Autono \n(2) Manual:")
    if a == "2":
        setManual()
    elif a == "1":
        setAutonomo()
