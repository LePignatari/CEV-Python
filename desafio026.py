frase = str(input('Escreva uma frase: ')).lower().strip()
print('Números de letras A presentes na frase: {}'.format(frase.count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print('A última letra A apreceu na posição: {}'.format(frase.rfind('a')+1))
