# coding: utf-8

import os

numerofatorial = int(raw_input("Calcule o fatorial de : "))
numeroAcumulador = 1
acumuladorProduto = 1

while numeroAcumulador <= numerofatorial:
    acumuladorProduto = acumuladorProduto * numeroAcumulador
    numeroAcumulador += 1

print (acumuladorProduto)
