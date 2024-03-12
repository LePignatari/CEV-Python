'''Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados, e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
num1 = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in num1:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi: {max(num1)} ')
print(f'O menor valor sorteado foi: {min(num1)}')
