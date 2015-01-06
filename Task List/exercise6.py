# coding: utf-8

maiorNumero = 0
contador = 1

while contador <= 3:
    numero = int(raw_input('Digite o %s º número : ' % str(contador)))

    if numero > maiorNumero:
        maiorNumero = numero


    contador += 1

print ('Maior número é %d ' % maiorNumero)
