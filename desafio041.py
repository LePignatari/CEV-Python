'''
Desafio 041: A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
→ Até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JUNIOR, até 25 anos: SÊNIOR, acima: MASTER.
'''

from datetime import date
ano = date.today().year
print('-=-'*10)
nas = int(input('Digite seu ano de nascimento: '))
i = ano - nas
print('-=-'*10)

print(f'Idade: {i}')

if i <= 9:
    print('\033[36mClassificação:\033[m MIRIM.')
elif i <= 14:
    print('\033[36mClassificação:\033[m INFANTIL.')
elif i <= 19:
    print('\033[36mClassificação:\033[m JUNIOR.')
elif i == 25:
    print('\033[36mClassificação:\033[m SÊNIOR.')
else:
    print('\033[36mClassificação:\033[m MASTER.')
