# coding: utf-8

import os

quantidadeDeIteracoes = 1
numeroMaximoDeIteracoes = int(raw_input('Digite o número máximo de iteracoes: '))

while quantidadeDeIteracoes <= numeroMaximoDeIteracoes:
    print ('Iteracao %d de %d ' % (quantidadeDeIteracoes, numeroMaximoDeIteracoes))
    quantidadeDeIteracoes += 1