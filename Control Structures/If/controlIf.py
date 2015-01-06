# coding: utf-8
velocidade = int(raw_input('Velocidade: '))

if velocidade > 110:
    print ('Você foi multado!')
    multa = (velocidade - 110) * 5.00
    print ('valor da multa: R$ %5.2f' % multa)
else:
    print ('Velocidade Permitida!')