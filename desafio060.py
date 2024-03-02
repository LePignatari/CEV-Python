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
