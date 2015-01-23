# coding: utf-8

from random import randint

sorteado = randint(1, 30)

print("Bem Vindo")

chute = []

while chute != sorteado:

    chute = raw_input("Digite um número: ").split(' ')

    if chute > sorteado:
        print("Mais baixo!")
    elif chute < sorteado:
        print("Mais Alto!")
    else:
        print("Acertou ! ")
        print("o número é %d" % chute)

print ("Fim")