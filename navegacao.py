
class Navegacao:

    def __init__(self,robo,coordAtual):
        self.coordAtual = coordAtual
        self.mover = robo

    def getCoord(self):
        return self.coordAtual

    def setNe(self, coord, nav):
        self.coordAtual = coord
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
        return self.getCoord()

    # Caso (x+,y-)
    def setSe(self, coord, nav):
        self.coordAtual = coord
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
        return self.getCoord()

    # Caso (x-, y+)
    def setNo(self, coord, nav):
        self.coordAtual = coord
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
        return self.getCoord()

    # Caso (x-, y-)
    def setSo(self, coord, nav):

        self.coordAtual = coord
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
        return self.getCoord()