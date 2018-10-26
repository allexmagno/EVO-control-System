from movimento import *
from quadrante import *
from navegacao import *


class Autonomo:
    def __init__(self, coordAtual, coordInicial, coordAdv, sequencia, robo):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv
        self.nav = Navegacao(robo, self.coordAtual)

        self.mover = Movimento('outA', 'outD', 200)
        self.mover = robo
        self.cacasEncontradas = 0

    def setCoordenada(self, coordenada):
        self.nav.setCoord(coordenada)

    def getCoordenada(self):
        return self.nav.getCoord().toString()

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
        # a = quadrante(0,self.sequencia)
        # a.dividirCacas()

        # verifica se possui caças definida no jogo
        if len(self.sequencia) == 0:
            return "Lista de cacas nao definida."

        # while len(self.sequencia) > 0:
        #
        #            if(len(a.quadB) >= len(a.quadC)):
        #                self.setEstrategia(a.quadB)
        #                if(len(a.quadIgnorado) > len(a.quadA)):
        #                    self.setEstrategia(a.quadIgnorado)
        #                else:
        #                    self.setEstrategia(a.quadA)
        #            else:
        #                self.setEstrategia(a.quadC)
        #                if (len(a.quadIgnorado) > len(a.quadA)):
        #                    self.setEstrategia(a.quadIgnorado)
        #                else:
        #                    self.setEstrategia(a.quadA)

        while len(self.sequencia) > 0:
            self.sequencia.sort()

            self.setEstrategia()

            #####################################
            ##TUDO que começa com 2 ## JA ESTAVA COMENTADO############
            ######################

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


            print("CoordAtual " + self.getCoordenada())
        return "Fim de jogo! \n Total de cacas encontradas: {}".format(self.cacasEncontradas)

    def setEstrategia(self):
        i = 0
        j = 0

        x_atual = self.coordAtual.getX()
        y_atual = self.coordAtual.getY()

        aux = (((self.sequencia[0].getX() - x_atual) ** 2) + (self.sequencia[0].getY() - y_atual) ** 2) ** (1 / 2)
        while i < (len(self.sequencia)):

            if aux > (((self.sequencia[i].getX() - x_atual) ** 2) + (self.sequencia[i].getY() - y_atual) ** 2) ** (
                        1 / 2):
                aux = (((self.sequencia[i].getX() - x_atual) ** 2) + (self.sequencia[i].getY() - y_atual) ** 2) ** (
                    1 / 2)
                j = i
            i = i + 1

        x = self.sequencia[j].getX() - self.nav.getCoord().getX()
        y = self.sequencia[j].getY() - self.nav.getCoord().getY()

        print(x)
        print(y)
        if (x > 0 and y > 0):
            print("Ne")
            self.nav.setNe(x, y, 1)
        if (x > 0 and y < 0):
            print("Se")
            self.nav.setSe(x, y, 1)
        if (x < 0 and y > 0):
            print("No")
            self.nav.setNo(x, y, 1)
        if (x < 0 and y < 0):
            print("So")
            self.nav.setSo(x, y, 1)
        if (x == 0):
            if (y > 0):
                print("N")
                self.nav.setNe(x, y, 1)
            if (y < 0):
                print("S")
                self.nav.setSe(x, y, 1)
        if (y == 0):
            if (x > 0):
                print("L")
                self.nav.setNe(x, y, 1)
            if (x < 0):
                print("O")
                self.nav.setSo(x, y, 1)
        print("caca aqui " + self.sequencia[j].toString())
        del self.sequencia[j]

        self.coordAtual = self.nav.getCoord()