# coding: utf-8

lista = []

contador = 0

while contador < 10:

    numero = float(raw_input('Digite o valor do %s º numero: ' % str(contador + 1)))
    lista.append(numero)

    contador += 1

print ('vetor digitado : ', lista)
print ('vetor invertido : ', lista[::-1])