# coding: utf-8

lista = [10, 10, 10, 10, 9]

soma = 0.00
media = 0.00

contador = 0

while contador <= 4:
    soma += lista[contador]
    contador += 1

media = soma / 5

print ('Media das 5 notas %5.2f ' % media)