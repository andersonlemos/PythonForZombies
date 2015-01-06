# coding: utf-8

minutosNaConta = int(raw_input('Quantidade de minutos na conta de telefone: '))
valorDaTarifa = 0

if minutosNaConta < 200:
    valorDaTarifa = 0.20
elif minutosNaConta < 400:
    valorDaTarifa = 0.18
elif minutosNaConta > 800:
    valorDaTarifa = 0.08
else:
    valorDaTarifa = 0.15

valorDaConta = minutosNaConta * valorDaTarifa

print('valor da conta é de R$ %5.2f' % valorDaConta)