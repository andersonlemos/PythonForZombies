# coding: utf-8

primeiro = int(raw_input('Primeiro : '))
segundo = int(raw_input('Segundo : '))
terceiro = int(raw_input('Terceiro : '))

if segundo < primeiro > terceiro:
    print ('Primeiro maior %d ' % primeiro)
elif primeiro < segundo > terceiro:
    print ('Segundo maior %d ' % segundo)
else:
    print('Terceiro maior %d ' % terceiro)


if segundo > primeiro < terceiro:
    print ('Primeiro menor %d ' % primeiro)
elif primeiro > segundo < terceiro:
    print ('Segundo menor %d ' % segundo)
else:
    print('Terceiro menor %d ' % terceiro)