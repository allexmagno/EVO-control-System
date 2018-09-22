from navegacao import *
from movimento import *
from autonomo import *
import threading
from manual import *
robot = Movimento('outA', 'outD', 200)
colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')
sc = ColorSensor()
sc.mode = 'COL-COLOR'
manual = Manual(robot)

def setNavegacao():
    s = int(input("1 (Ne), 2 (Se), 3 (No), 4 (So)\n"))
    t1 = int(input("x: "))
    t2 = int(input("y: "))
    t3 = int(input("nav: "))

    if s == 1:
        nav.setNe(t1, t2, t3)
    elif s == 2:
        nav.setSe(t1, t2, t3)
    elif s == 3:
        nav.setNo(t1, t2, t3)
    elif s == 4:
        nav.setSo(t1, t2, t3)


def setManual():
    print(
        "selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Retornar \n space - Parar \n")
    op = input("digite uma opcao:")

    if op == "a":
        robot.setEsquerda()

    if op == "d":
        robot.setDireita()

    if op == "w":
        robot.setFrente()

    if op == "s":
        robot.setRetornar()

    if op == chr(32):
        robot.setParar()

def exe():
    print(aut.executar())

c1 = Coordenadas(0, 0, "L")
c2 = Coordenadas(0, 0, "L")
c3 = Coordenadas(6, 6, 'O')
s = [Coordenadas(0,6," "),Coordenadas(2,1," "),Coordenadas(4,0," "),Coordenadas(6,1," "),Coordenadas(3,5," "), Coordenadas(5,5, " "), Coordenadas(2,2, " "), Coordenadas(1,0, " "), Coordenadas(6,6, " ")]
aut = Autonomo(c1, c2, c3, s, robot)
nav = Navegacao(robot,c1)
while (True):
    if colors[sc.value()] == "yellow":
        dir = input("Posicao inicial (0,0). informe direcao: ")
        c1 = Coordenadas(0, 0, dir)

    if colors[sc.value()] == "blue":
        dir = input("Posicao inicial (6,6). informe direcao: ")
        c1 = Coordenadas(6, 6, dir)


    print("Posicao atual: " + aut.getCoordenada())
    corrigir = input("Corrigir posicao? s ou n: ")
    if corrigir == "s":
        x = int(input("X atual: "))
        y = int(input("Y atual: "))
        dir = input("Direcao: ")
        print("Posicao atual ({},{},{})".format(x,y,dir))
        c1 = Coordenadas(x, y, dir)


        aut = Autonomo(c1, c2, c3, s, robot)

    a = input("(1) Autono \n(2) Manual: \n(3) Autonomo.exe")
    if a == "2":
        setManual()

    elif a == "1":
        setAutonomo()

    elif a == "3":
        exe()