'''
Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre: 
→ quantas vezes a letra “a” aparece. 
→ Em que posição ela aparece a primeira vez. 
→ Em que posição ela aparece a última vez.
'''

frase = str(input('Escreva uma frase: ')).lower().strip()
print('Números de letras A presentes na frase: {}'.format(frase.count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print('A última letra A apreceu na posição: {}'.format(frase.rfind('a')+1))
