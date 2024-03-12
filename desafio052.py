'''
Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo ( números divisíveis por 1 e ele mesmo).
'''

print('\033[33m-=-' * 10)
print(f'{' ':>3}DESCOBRINDO SE É PRIMO')
print('-=-' * 10)

print('\033[35mCondições: ser divísivel somente por 1 e ele mesmo.\033[m')
num = int(input('Informe um número: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        cont += +1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if cont == 2:
    print(f'\n\033[mO número {num} foi divídido \033[32m{cont} vezes\033[m, e por isso...')
    print('Ele é um número primo!')
else:
    print(f'\n\033[mO número {num} foi divídido \033[31m{cont} vezes\033[m, e por isso...')
    print('Ele não é um número primo!')
