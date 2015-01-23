# coding: utf-8

from random import randint

sorteado = randint(1, 100)

print("Bem Vindo")

chute = 0

while chute != sorteado:

    chute = int(raw_input("Digite um número: "))

    if chute > sorteado:
        print("Mais baixo!")
    elif chute < sorteado:
        print("Mais Alto!")
    else:
        print("Acertou ! ")
        print("o número é %d" % chute)

print ("Fim")