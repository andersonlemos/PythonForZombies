# coding: utf-8

ladoA = float(raw_input('Digite o tamanho do primero lado : '))
ladoB = float(raw_input('Digite o tamanho do segundo lado : '))
ladoC = float(raw_input('Digite o tamanho do terceiro lado : '))

if ladoC > ladoA + ladoB or ladoA > ladoB + ladoC or ladoB > ladoA + ladoC:
    print ('Não é um triângulo!')
elif ladoA == ladoB == ladoC:
    print('Equilatero')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print ('Isosceles')
else:
    print ('Escaleno')