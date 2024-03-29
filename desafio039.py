'''
Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
→ Se ele ainda vai se alistar ao serviço militar, Se é a hora de se alistar, Se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
''' 

from datetime import date
print('\033[31m-=-'*6)
print('DIA DO ALISTAMENTO')
print('-=-'*6)

ano = int(input('\033[mData de nascimento: '))
hoje = date.today().year
i = hoje - ano

print(f'Você nasceu em {ano} e tem {i} em {hoje}, portanto:')
if i < 18:
    print('Ainda \033[31mnão pode\033[m fazer o alistamento.')
    print(f'Faltam \033[36m{18 - i} ano(s)\033[m para ser liberado.')
elif i == 18:
    print('Já é \033[31mhora de se alistar\033[m.')
elif i > 18:
    print(f'\033[31mJá passou\033[m \033[36m{i - 18} ano(s)\033[m do seu alistamento.')
