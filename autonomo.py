from movimento import *
from quadrante import *


class Autonomo:
    def __init__(self, coordAtual, coordInicial, coordAdv, sequencia, robo):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv

        self.mover = Movimento('outA', 'outD', 200)

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

    def calculaDistancia(self, c1, c2):
        aux = (((c1.getX() - c2.getX()) ** 2) + (c1.getY() - c2.getY()) ** 2) ** (1 / 2)
        return aux


    def executar(self):
        a = quadrante(0,self.sequencia)
        a.dividirCacas()

        # verifica se possui caças definida no jogo
        if len(self.sequencia) == 0:
            return "Lista de cacas nao definida."

        while len(self.sequencia) > 0:

            self.sequencia.sort()

            i = 0
            while i in range(len(self.sequencia)):
                mx = self.sequencia(0).getX - self.coordAtual.getX
                my = self.sequencia(0).getY - self.coordAtual.getY


            if(len(a.quadB) >= len(a.quadC)):
                self.setEstrategia_Raio(a.quadB)
                if(len(a.quadIgnorado) > len(a.quadA)):
                    self.setEstrategia_Raio(a.quadIgnorado)
                else:
                    self.setEstrategia_Raio(a.quadA)
            else:
                self.setEstrategia_Raio(a.quadC)
                if (len(a.quadIgnorado) > len(a.quadA)):
                    self.setEstrategia_Raio(a.quadIgnorado)
                else:
                    self.setEstrategia_Raio(a.quadA)

        #while len(self.sequencia) > 0:
            #self.sequencia.sort()

            #self.setEstrategia_1()

            #####################################
            ##TUDO que começa com 2 ## JA ESTAVA COMENTADO############
            ######################3

            ##if self.setValidar():
            ##    self.cacasEncontradas = self.cacasEncontradas + 1
            ##else:
            ##    print("Caça não vadidada pelo SS! \n")
            ##    print("Verifique coordenadas: {}.\n".format(self.coordAtual.toString))
            ##    verifica = input("Esta é sua coordenada atual?\n(s) Sim\n(n)Não\n")
            ##    if verifica == "n":
            ##        novo_x = input("Valor de x: ")
            ##        novo_y = input("Valor de y: ")
            # #       novo_o = input("Orientação (N,S,L,O): ")
            # #       self.setCoordenada(Coordenadas(novo_x,novo_y,novo_o))


            #print ("CoordAtual "+ self.getCoordenada())
        return "Fim de jogo! \n Total de cacas encontradas: {}".format(self.cacasEncontradas)


    def setEstrategia_Raio(self,listaQuadrante):
        i = 0
        j = 0

        x_atual = self.coordAtual.getX()
        y_atual = self.coordAtual.getY()

        aux = (((listaQuadrante.getX() - x_atual) ** 2) + (listaQuadrante.getY() - y_atual) ** 2) ** (1 / 2)
        while i < (len(listaQuadrante)):

            if aux > (((listaQuadrante.getX() - x_atual)**2) + (listaQuadrante.getY() - y_atual)**2)**(1/2):
                aux = (((listaQuadrante.getX() - x_atual)**2) + (listaQuadrante.getY() - y_atual)**2)**(1/2)
                j = i
            i = i + 1

        xc = listaQuadrante[j].getX() - self.coordAtual.getX()
        xy = listaQuadrante[j].getY() - self.coordAtual.getY()

        print(xc)
        print(xy)
        if(xc > 0 and xy > 0):
            print ("Ne")
            self.setNe(xc,xy,1)
        if(xc > 0 and xy < 0):
            print ("Se")
            self.setSe(xc,xy,1)
        if(xc < 0 and xy > 0):
            print ("No")
            self.setNo(xc,xy,1)
        if (xc < 0 and xy < 0):
            print ("So")
            self.setSo(xc,xy,1)
        if(xc == 0):
            if(xy > 0):
                print ("N")
                self.setNe(xc,xy,1)
            if(xy < 0):
                print ("S")
                self.setSe(xc,xy,1)
        if(xy == 0):
            if(xc > 0):
                print ("L")
                self.setNe(xc,xy,1)
            if(xc < 0):
                print ("O")
                self.setSo(xc,xy,1)
        print ("caca aqui "+self.sequencia[j].toString())

        iterador = 0
        while iterador <= len(self.sequencia) :
            if(listaQuadrante[j] == self.sequencia[iterador]):
                del self.sequencia[iterador]
                iterador = iterador + 1
                break
            iterador = iterador + 1
        del listaQuadrante[j]




    # Estratigia p/ quando inimigo longe
    def setEstrategia_1(self):
        i = 0
        j = 0

        x_atual = self.coordAtual.getX()
        y_atual = self.coordAtual.getY()

        aux = (((self.sequencia[0].getX() - x_atual)** 2) + (self.sequencia[0].getY() - y_atual) ** 2) ** (1 / 2)
        while i < (len(self.sequencia)):

            if aux > (((self.sequencia[i].getX() - x_atual)**2) + (self.sequencia[i].getY() - y_atual)**2)**(1/2):
                aux = (((self.sequencia[i].getX() - x_atual)**2) + (self.sequencia[i].getY() - y_atual)**2)**(1/2)
                j = i
            i = i + 1

        xc = self.sequencia[j].getX() - self.coordAtual.getX()
        xy = self.sequencia[j].getY() - self.coordAtual.getY()

        print(xc)
        print(xy)
        if(xc > 0 and xy > 0):
            print ("Ne")
            self.setNe(xc,xy,1)
        if(xc > 0 and xy < 0):
            print ("Se")
            self.setSe(xc,xy,1)
        if(xc < 0 and xy > 0):
            print ("No")
            self.setNo(xc,xy,1)
        if (xc < 0 and xy < 0):
            print ("So")
            self.setSo(xc,xy,1)
        if(xc == 0):
            if(xy > 0):
                print ("N")
                self.setNe(xc,xy,1)
            if(xy < 0):
                print ("S")
                self.setSe(xc,xy,1)
        if(xy == 0):
            if(xc > 0):
                print ("L")
                self.setNe(xc,xy,1)
            if(xc < 0):
                print ("O")
                self.setSo(xc,xy,1)
        print ("caca aqui "+self.sequencia[j].toString())
        del self.sequencia[j]

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

            if y < 0:
                self.mover.setDireita()
                self.coordAtual.setOr('S')
                self.coordAtual.setY(self.coordAtual.getY() - 1)
                y = y + 1
                while y < 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY() - 1)

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
                self.mover.setEsquerda()
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
                self.mover.setDireita()
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


    #caso (x+, y+)
    def setNordeste(self, x, y, orientacao, nav):
        if nav == 1:
            if self.coordAtual.getOr == 'N':
                while y > 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY + 1)

            if self.coordAtual.getOr == 'S':
                self.mover.setRetornar()
                y = y + 1
                self.coordAtual.setOr('N')
                while y > 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY + 1)

            if self.coordAtual.getOr == 'L':
                self.mover.setEsquerda()
                y = y + 1
                self.coordAtual.setOr('N')
                while y > 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY + 1)

            if self.coordAtual.getOr == 'O':
                self.mover.setDireita()
                y = y + 1
                self.coordAtual.setOr('N')
                while y > 0:
                    self.mover.setFrente()
                    y = y + 1
                    self.coordAtual.setY(self.coordAtual.getY + 1)


            self.mover.setDireita()
            self.coordAtual.setOr('L')
            x = x + 1
            while x > 0:
                self.mover.setFrente()
                x = x + 1
                self.coordAtual.setX(self.coordAtual + 1)

        elif nav == 2:
            self.mover.setEsquerda()
            self.coordAtual.setOr('N')
            y = y + 1
            while y > 0:
                self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual + 1)

    # Caso (x+,y-)
    def setSudeste(self, x, y, orientacao, nav):
        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                #self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX+1)

            #self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                #self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'O' and nav == 1:
            #self.mover.Retornar()
            x = x - 1
            self.coordAtual.setOr('L')
            while x > 0:
                #self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            #self.mover.setDireita()
            self.coordAtual.setOr('L')
            y = y + 1
            while y < 0:
                #self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                #self.mover.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            #self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                #self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)

        if self.coordAtual.getOr == 'L' and nav == 1:
            while x > 0:
                #ver.setFrente()
                x = x - 1
                self.coordAtual.setX(self.coordAtual.getX + 1)

            #self.mover.setDireita()
            self.coordAtual.setOr('S')
            y = y + 1
            while y < 0:
                #self.mover.setFrente()
                y = y + 1
                self.coordAtual.setY(self.coordAtual.getY - 1)
    # Caso (x-, y+)
    def setSudeste(self, x, y, orientacao):
        pass

    # Caso (x-, y-)
    def setSudoeste(self, x, y, orientacao):
      pass
