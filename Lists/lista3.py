# coding: utf-8

lista = []

contador = 0

while contador < 5:

    lista.append(int(raw_input('Digite o valor do %s º número : ' % str(contador + 1))))
    contador += 1

print ('Veto lido ', lista)

