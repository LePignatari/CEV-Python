'''
Desafio 04: programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as possíveis informações. 
'''

n = input('Digite algo: ')
print('Totalmente em maiúsculo?: {}'.format(n.isupper()))
print('Totalmente em minúsculo?: {}'.format(n.islower()))
print('Possui números e letras?: {}'.format(n.isalnum()))
print('É numérico?: {}'.format(n.isnumeric()))
print('Possui somente letras?: {}'.format(n.isalpha()))
print('Está capitalizada?: {}'.format(n.istitle()))
