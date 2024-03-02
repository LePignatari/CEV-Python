'''
Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial, exemplo: 5! = 5x4x3x2x1 = 120.
>>> Usando WHILE, com biblíoteca:
'''

from math import factorial
print('\033[35m-=-' * 15)
print(f'{' ':>10}CALCULANDO O FATORIAL')
print('-=-' * 15)

num = int(input('\033[mDigite um número para calcular o fatorial: '))
cont = num
print(f'\033[32mCalculando {num}!\033[m =', end=' ')

while cont > 0:
    print(f'{cont}', end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')  # isso eu não tinha colocado antes, peguei a dica!
    cont -= 1
print(f'{factorial(num)}')
