import threading
from time import sleep

def setDireita():
    i = 0
    while i < 5:
        print("direita")
        i = i + 1
        sleep(0.5)

def setEsquerda():
    i = 0
    while i < 5:
        print("esquerda")
        i = i + 1
        sleep(0.5)

def setFrente():
    i = 0
    while i < 5:
        print("Frente")
        i = i + 1
        sleep(0.5)

def setRetornar():
    i = 0
    while i < 5:
        print("retornar")
        i = i + 1
        sleep(0.5)

def setParar():
    i = 0
    while i < 5:
        print("parar")
        i = i + 1
        sleep(0.5)


def setAutonomo():
    s = int(input("1 (Ne), 2 (Se), 3 (No), 4 (Ne)"))
    t1 = int(input("x: "))
    t2 = int(input("y: "))
    t3 = int(input("nav: "))

    if s == 1:
        print("s = 1")
    elif s == 2:
        print("s = 2")
    elif s == 3:
        print("s = 3")
    elif s == 4:
        print("s = 4")



def setManual():
    print(
        "selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Retornar \n space - Parar \n")
    op = input("digite uma opcao:")

    if op == "a":
        a = threading.Thread(target=setEsquerda)
        a.start()

    if op == "d":
        d = threading.Thread(target=setDireita)
        d.start()
    if op == "w":
        w = threading.Thread(target=setFrente)
        w.start()

    if op == "s":
        s = threading.Thread(target=setRetornar)
        s.start()

    if op == chr(32):
        spc = threading.Thread(target=setParar)
        spc.start()


while (True):
    a = input("(1) Autonomo \n(2) Manual:")
    if a == "2":
        setManual()
    elif a == "1":
        setAutonomo()
