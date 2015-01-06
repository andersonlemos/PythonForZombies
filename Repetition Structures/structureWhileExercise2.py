# coding: utf-8
import os

numeroMaximo = int(raw_input('Digite o último número: '))
numeroDeIteracoes = 1

while numeroDeIteracoes <= numeroMaximo:
    if numeroDeIteracoes % 2 == 0:
        print(numeroDeIteracoes)
    numeroDeIteracoes += 1