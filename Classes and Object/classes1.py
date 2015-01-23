#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
class Pessoa():
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self):
        dataAtual = datetime.date.today() - self.nascimento
        return int(dataAtual.days/365)

    def __str__(self):
        return '%s , %d anos' %(self.nome,self.idade())

masanori = Pessoa('Dunha Silva',datetime.date(1980,9,1))

print masanori.idade()
print masanori

