# coding: utf-8
import os

contador = 1
maiorNumero = 0

while contador <= 3:
    inputNumber = int(raw_input("Digite um número inteiro: "))

    if inputNumber > maiorNumero:
        maiorNumero = inputNumber

    contador += 1
print('O maior número digitado foi : %d' % maiorNumero)


