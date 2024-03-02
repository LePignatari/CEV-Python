'''
Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (frases que podem ser lidas de trás para frente, ex: após a sopa.), desconsiderando os espaços.
>>> Usando o for:
'''

frase = str(input('Escreva uma frase: ')).strip().split()
frase_junta = ''.join(frase).upper()
inverte = ''
for letra in range(len(frase_junta) - 1, -1, -1):
    inverte += frase_junta[letra]
print(f'O inverso de {frase_junta} é {inverte}.')
if inverte == frase_junta:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
