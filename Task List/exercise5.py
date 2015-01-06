# coding: utf-8
import os, math

peso = int(raw_input("Quantidade de Quilos pescada : "))

excedente = 'ZERO'
multa = 'ZERO'

if peso > 50:
    excedente = peso - 50.00
    multa = excedente * 4.00

print ('Peso Excedente %s Kg(s)' % str(excedente))
print ('Valor da Multa R$ %s ' % str(multa))
