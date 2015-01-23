# coding: utf-8


print ("====== Bem vindo! ======")

chute = 0

while chute != 42:

    chute = int(raw_input("Qual é o número:"))

    if chute > 42:
        print("Mais baixo")
    elif chute < 42:
        print("Mais Alto")
    else:
        print("Acertou!")

print ("===== FIM DO JOGO ======")