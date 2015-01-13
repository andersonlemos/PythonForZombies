# coding: utf-8


def ePar(numero):

    return (numero % 2) == 0


x = int(raw_input("Digite um numero: "))

if ePar(x):
    print("É Par")
else:
    print("É impar")



