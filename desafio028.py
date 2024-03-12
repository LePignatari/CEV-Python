'''
Desafio 028: Escreva um programa que faça o computador ‘pensar’ em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
print('\033[33m-=-\033[m'*13)
print('JOGO DE ADIVINHAÇÃO!')
print('\033[34mPensando em um número entre 0 e 5...\033[m')
print('\033[33m-=-\033[m'*13)

num = int(input('Digite o seu palpite: '))
esc = randint(0, 5)

if num == esc:
    print('O seu palpite foi certeiro! Parabéns!')
    print('\033[32mVOCÊ VENCEU')
else:
    print(f'Eu pensei no número \033[32m{esc}\033[m não no número \033[31m{num}\033[m!')
    print('\033[31mVOCÊ PERDEU')
