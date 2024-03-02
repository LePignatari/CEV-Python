'''
Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

print('\033[35m>-=-<'*3)
print('ANO BISSEXTO')
print('>-=-<'*3)

a = int(input('\033[mDigite o ano que vamos analisar ou coloque 0 para analisar o ano atual: '))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano de \033[31m{a}\033[m é um ano \033[34mBISSEXTO\033[m!')
else:
    print(f'O ano de \033[31m{a}\033[m não é um ano \033[34mBISSEXTO\033[m!')
