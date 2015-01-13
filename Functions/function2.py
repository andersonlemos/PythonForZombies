# coding: utf-8

def fatorial(numero):

  acumuladorProduto = 1

  for numeroAcumulador in range(numero):
      acumuladorProduto *= numeroAcumulador+1

  return acumuladorProduto

print (fatorial(10))