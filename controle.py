from navegacao import *
from movimento import *
from autonomo import *
import threading
from manual import *
from coordenadas import *


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

def exe():
    print(aut.executar())

c1 = Coordenadas(0, 0, "L")
c2 = Coordenadas(0, 0, "L")
c3 = Coordenadas(6, 6, 'O')
c4 = Coordenadas(0, 6, ' ')
c5 = Coordenadas(3, 3, ' ')
c6 = Coordenadas(6, 0, ' ')
c7 = Coordenadas(1, 1, ' ')
c8 = Coordenadas(2, 2, ' ')
c9 = Coordenadas(5, 6, ' ')



s = [c4, c5, c6, c7, c8, c9]
aut = Autonomo(c1, c2, c3, s, robot)
nav = Navegacao(robot, c1)


while True:
    a = input("(1) Autonomo \n(2) Manual: \n(3) Autonomo.exe")
    if a == "2":

       manual.comandos()

    if a == 1:
        if colors[sc.value()] == "yellow":
            dir = input("Posicao inicial (0,0). informe direcao: ")
            c1 = Coordenadas(0, 0, dir)

        if colors[sc.value()] == "blue":
            dir = input("Posicao inicial (6,6). informe direcao: ")
            c1 = Coordenadas(6, 6, dir)


        print("Posicao atual: " + nav.getCoordenada())

        corrigir = input("Corrigir posicao? s ou n: ")
        if corrigir == "s":
            x = int(input("X atual: "))
            y = int(input("Y atual: "))
            dir = input("Direcao: ")
            print("Posicao atual ({},{},{})".format(x,y,dir))
            c1 = Coordenadas(x, y, dir)
            aut.setCoordenada(c1)

        b = input("(1) Autonomo \n(3) Autonomo \n")
        if b == 1:
            setNavegacao()
        elif b == 2:
            exe()