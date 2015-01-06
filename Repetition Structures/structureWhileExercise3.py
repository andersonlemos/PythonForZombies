# coding: utf-8

import os

tabuada = 1
multiplicador = 0

while tabuada <= 10:

    print('Tabuada de %d ' % tabuada)

    multiplicador = 1

    while multiplicador <= 10:
        print ('%d x %d = %d' % (tabuada, multiplicador, tabuada*multiplicador))
        multiplicador += 1

    tabuada += 1
