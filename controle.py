from movimento import *
import threading

robot = Movimento('outA', 'outD', 200)

print("selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Parar \n")

while (True):

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
