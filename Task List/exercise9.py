#coding: utf-8
numero = int(raw_input("Digite um numero  :"))
soma = 0
contador = 1

while contador < numero:
    soma = numero * (contador + 1) * (contador + 2)

    if soma == numero:
        print("É triangular")
        break
    else:
        print("Não é triangular")
        break
    contador += 1



