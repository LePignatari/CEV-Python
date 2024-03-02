'''
Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (frases que podem ser lidas de trás para frente, ex: após a sopa.), desconsiderando os espaços.
>>> Sem uso do for:
'''

frase = str(input('Escreva uma frase: ')).strip().split()
frase_junta = ''.join(frase).upper()  # isso faz com que a frase vire uma coisa só (junta).
frase_invertida = frase_junta[::-1]   # vai ler a frase de trás para frente.

print(f'O inverso de {frase_junta} é {frase_invertida}')

if frase_invertida == frase_junta:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
