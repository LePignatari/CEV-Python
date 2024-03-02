'''
Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome “SANTO”.
'''

nome = str(input('Digite o nome de uma cidade: ')).strip()
div = (nome.lower().split())
print('A cidade começa com SANTO?: {}'.format('santo' in div[0]))
