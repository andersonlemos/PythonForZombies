# coding: utf-8


def embaralha(palavra):
    import random
    lista = list(palavra)

    random.shuffle(lista)

    return ''.join(lista)


frase = raw_input("Digite uma palavra : ")

print(embaralha(frase))