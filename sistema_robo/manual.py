
class Manual:

    def __init__(self,robot):
        self.robot = robot

    def setEsquerda(self):
        self.robot.setEsquerda()

    def setDireita(self):
        self.robot.setDireita()

    def setFrente(self):
        self.robot.setFrente()

    def setRetornar(self):
        self.robot.setRetornar()

    def setParar(self):
        self.robot.setParar()

    def comandos(self):
        print(
            "selecione um movimento:\n a - esquerda\n d - direita\n w - seguir em frente\n s - Retornar \n space - Parar \n")
        op = input("digite uma opcao:")

        if op == "a":
            self.robot.setEsquerda()

        if op == "d":
            self.robot.setDireita()

        if op == "w":
            self.robot.setFrente()

        if op == "s":
            self.robot.setRetornar()

        if op == chr(32):
            self.robot.setParar()