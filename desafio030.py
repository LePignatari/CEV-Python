'''
Desafio 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

print('\033[35m¨'*15)
print('PAR OU ÍMPAR?')
print('¨'*15)

num = int(input('\033[mDigite um número inteiro: '))
par = num % 2

if par == 0:
    print(f'\033[36m{num}\033[m é um número \033[32mPAR\033[m!')
else:
    print(f'\033[36m{num}\033[m é um número \033[32mÍMPAR\033[m!')
