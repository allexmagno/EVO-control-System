#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

class SeguirLinha:

    def __init__(self, cor):
        self.cor = cor

    def encontrarLinha(self):

