# coding: utf-8
import os, math

tamanhoMetrosQuadrados = float(raw_input("Digite o tamanho em m2: "))
litrosDeTinta = tamanhoMetrosQuadrados / 3.00
latasDeTinta = math.ceil(litrosDeTinta / 18.00)
valorLatasDeTinta = latasDeTinta * 80.00

print ('Litros de tinta %5.2f ' % litrosDeTinta)
print ('Latas de tinta %5.2f ' % latasDeTinta)
print ('TOTAL R$ %5.2f ' % valorLatasDeTinta)