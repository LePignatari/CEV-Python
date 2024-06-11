from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for s in range(5):
        sorteio = randint(1, 10)
        numeros.append(sorteio)
        print(sorteio, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(soma, end='')


numeros = list()
sorteia(numeros)
somaPar(numeros)
