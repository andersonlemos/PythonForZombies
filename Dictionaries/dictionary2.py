#coding: utf-8

arquivo = open('alice.txt')

texto = arquivo.read()
texto = texto.lower()

import string

for palavra in string.punctuation:
    texto = texto.replace(palavra,' ')
texto =  texto.split()

dic = {}

for p in texto:
    if p not in  dic:
        dic[p] = 1
    else:
        dic[p] += 1


print(dic)