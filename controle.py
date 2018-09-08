from movimento import *


robot = Movimento('outA','outD',200)


print("selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Parar \n")


while (True):

	op = input("digite uma opcao:")

	if op == "a":
		robot.setParar()
		robot.setEsquerda()

	if op == "d":	
		robot.setParar()
		robot.setDireita()
	
	if op == "w":	
		robot.setFrente()

	if op== "s":
		robot.setRetornar()
