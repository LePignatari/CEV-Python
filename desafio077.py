'''Desafio 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

lista = ('aprender', 'programar', 'linguaguem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for palavras in lista:  # analisando cada elemento da tupla.
    print(f'\nNa palavra \033[33m{palavras.upper()}\033[m temos as vogais: ', end='')
    for letra in palavras:
        if letra in 'aeiou':    # analisando se cada letra esta dentro das vogais
            print(f'\033[36m{letra}\033[m', end=' ')    # caso esteja, ele ira escrever
