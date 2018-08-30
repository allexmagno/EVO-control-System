#!/usr/bin/env python3
from ev3dev.ev3 import *
from seguirlinha import *
from time import sleep


Class Movimento:

   # _l = LargerMotor('OutA')
   # _r = LargerMotor('OutD')
    _sl = SeguiLinha(2);

    def __init__(self, posicao, destino, velicidade):
        self.poscao = posicao
        self.destino = destino
        self.velocidade = velicidade

    def setFrente():
        while(seguirLinha()):
            l.run_forever(speed_sp=velocidade)
            r.run_forever(speed_sp=velocidade)

    def setDireita():
        l.run_forever(speed_sp=velocidade)

    def setEsquerda():
        r.run_forever(speed_sp=velocidade)

    def setRetornar():


    def setVelocidade(self, setV):
        self.velocidade = setV

    def setParar():
        r.stop(stop_action="hold")
        l.stop(stop_action="hold")