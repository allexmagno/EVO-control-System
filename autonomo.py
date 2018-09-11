


class Autonomo:

    def __init__(self, coordAtual, coordInicial, coordAdv, sequencia):
        self.coordAtual = coordAtual
        self.coordInicial = coordInicial
        self.sequencia = sequencia
        self.coordAdv = coordAdv

    def setCoordenada(self, coordenada):
        self.coordAtual = coordenada

    def getAversario(self, adv):
        self.coordAdv = adv

    def getSeqAtualizada(self):
        return self.sequencia

    def executar(self):
        while self.sequencia != 0:

            self.sequencia.sort()
            i = 0
            while i in range(len(self.sequencia)):
                mx = self.sequencia(0).getX - self.coordAtual.getX
                my = self.sequencia(0).getY - self.coordAtual.getY

                if (mx < 0 and self.coordAtual.getOr == 'N'):
                    pass
                if (mx < 0 and self.coordAtual.getOr == 'S'):
                    pass
                if (mx < 0 and self.coordAtual.getOr == 'L'):
                    pass
                if (mx < 0 and self.coordAtual.getOr == 'O'):
                    pass

                if (mx > 0 and self.coordAtual.getOr == 'N'):
                    pass
                if (mx > 0 and self.coordAtual.getOr == 'S'):
                    pass
                if (mx > 0 and self.coordAtual.getOr == 'L'):
                    pass
                if (mx > 0 and self.coordAtual.getOr == 'O'):
                    pass
          #  if(self.coordInicial.getX == 0 and self.coordInicial.getY == 0):

                if (my < 0 and self.coordAtual.getOr == 'N'):
                    pass
                if (my < 0 and self.coordAtual.getOr == 'S'):
                    pass
                if (my < 0 and self.coordAtual.getOr == 'L'):
                    pass
                if (my < 0 and self.coordAtual.getOr == 'O'):
                    pass

                if (my > 0 and self.coordAtual.getOr == 'N'):
                    pass
                if (my > 0 and self.coordAtual.getOr == 'S'):
                    pass
                if (my > 0 and self.coordAtual.getOr == 'L'):
                    pass
                if (my > 0 and self.coordAtual.getOr == 'O'):
                    pass

