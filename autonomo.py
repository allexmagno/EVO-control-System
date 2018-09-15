from movimento import *
from coordenadas import *

class Autonomo:
    def __init__(self, coordAtual, coordInicial, coordAdv, sequencia, robo):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv
        self.mover = robo
        self.cacasEncontradas = 0

    def setCoordenada(self, coordenada):
        self.coordAtual = coordenada

    def getCoordenada(self):
        return self.coordAtual.toString()

    def getAversario(self, adv):
        self.coordAdv = adv

    def getSeqAtualizada(self):
        return self.sequencia

    def setValidar(self):
        return self.coordAtual.toString()

    # Metodo principal onde ira verificar qual a melhor estrategia naquele dado momento
    def executar(self):

        # verifica se possui caças definida no jogo
        if self.sequencia == 0:
            return "Lista de caças não definida."

        while self.sequencia != 0:

            self.sequencia.sort()

            if self.coordAdv < self.coordAtual:
                self.setEstrategia_1()
            else:
                self.setEstrategia_2()

            if self.setValidar():
                self.cacasEncontradas = self.cacasEncontradas + 1
            else:
                print("Caça não vadidada pelo SS! \n")
                print("Verifique coordenadas: {}.\n".format(self.coordAtual.toString))
                verifica = input("Esta é sua coordenada atual?\n(s) Sim\n(n)Não\n")
                if verifica == "n":
                    novo_x = input("Valor de x: ")
                    novo_y = input("Valor de y: ")
                    novo_o = input("Orientação (N,S,L,O): ")
                    self.setCoordenada(Coordenadas(novo_x,novo_y,novo_o))

        return "Fim de jogo! \n Total de caças encontradas: {}".format(self.cacasEncontradas)


    # Estratigia p/ quando inimigo longe
    def setEstrategia_1(self):
        #
        # codigo (...)
        #
        pass


    # Estrategia p/ inimigo perto
    def setEstrategia_2(self):
        #
        # codigo (...)
        #
        pass

    # caso (x+, y+)
    def setNe(self, x, y, nav):
        if nav == 2:
            if self.coordAtual.getOr() == 'N':
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setRetornar()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setEsquerda()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setDireita()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if x > 0:
                self.mover.setDireita()
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                x = x - 1
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

        if nav == 1:
            if self.coordAtual.getOr() == 'L':
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setRetornar()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setEsquerda()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setDireita()
                x = x - 1
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if y > 0:
                self.mover.setEsquerda()
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                y = y - 1
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

    # Caso (x+,y-)
    def setSe(self, x, y, nav):
        if nav == 2:
            if self.coordAtual.getOr() == 'S':
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setRetornar()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setEsquerda()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setDireita()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if x > 0:
                self.mover.setEsquerda()
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                x = x - 1
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

        if nav == 1:
            if self.coordAtual.getOr() == 'L':
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setRetornar()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setEsquerda()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                self.coordAtual.setOr('L')
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setDireita()
                x = x - 1
                self.coordAtual.setOr('L')
                self.coordAtual.setX(self.coordAtual.getX() + 1)
                while x > 0:
                    self.mover.setFrente()
                    x = x - 1
                    self.coordAtual.setX(self.coordAtual.getX() + 1)

            if y > 0:
                self.mover.setDireita()
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                y = y - 1
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

    # Caso (x-, y+)
    def setNo(self, x, y, nav):
        if nav == 2:
            if self.coordAtual.getOr() == 'N':
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setRetornar()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setEsquerda()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setDireita()
                y = y - 1
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

            if x < 0:
                self.mover.setDireita()
                self.coordAtual.setOr('O')
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                x = x + 1
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

        if nav == 1:
            if self.coordAtual.getOr() == 'O':
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setRetornar()
                x = x + 1
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                self.coordAtual.setOr('O')
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setEsquerda()
                x = x + 1
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                self.coordAtual.setOr('O')
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setDireita()
                x = x + 1
                self.coordAtual.setOr('O')
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if y > 0:
                self.mover.setEsquerda()
                self.coordAtual.setOr('N')
                self.coordAtual.setY(self.coordAtual.getY() + 1)
                y = y - 1
                while y > 0:
                    self.mover.setFrente()
                    y = y - 1
                    self.coordAtual.setY(self.coordAtual.getY() + 1)

    # Caso (x-, y-)
    def setSo(self, x, y, nav):
        if nav == 2:
            if self.coordAtual.getOr() == 'S':
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setRetornar()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'O':
                self.mover.setEsquerda()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y > 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setDireita()
                y = y + 1
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

            if x < 0:
                self.mover.setDireita()
                self.coordAtual.setOr('O')
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                x = x + 1
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

        if nav == 1:
            if self.coordAtual.getOr() == 'O':
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'L':
                self.mover.setRetornar()
                x = x + 1
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                self.coordAtual.setOr('O')
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'N':
                self.mover.setEsquerda()
                x = x + 1
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                self.coordAtual.setOr('O')
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if self.coordAtual.getOr() == 'S':
                self.mover.setDireita()
                x = x + 1
                self.coordAtual.setOr('O')
                self.coordAtual.setX(self.coordAtual.getX() - 1)
                while x < 0:
                    self.mover.setFrente()
                    x = x + 1
                    self.coordAtual.setX(self.coordAtual.getX() - 1)

            if y < 0:
                self.mover.setEsquerda()
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                y = y + 1
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

