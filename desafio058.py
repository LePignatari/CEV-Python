from random import randint
from emoji import emojize
print('\033[35m-=-' * 15)
print('''Olá! Sou seu computador...
E eu acabei de pensar em um número entre \033[33m0 e 10!\033[m
\033[35mSerá que \033[32mvocê consegue adivinhar qual\033[35m foi ?!''')
print('-=-' * 15, '\033[m')
computador = randint(0, 10)
p = ''
cont = 0
print(' ')
while p != computador:
    p = int(input('⇨ Qual é o seu palpite?: '))
    cont += 1
    if p != computador:
        if p < computador:
            print('Tente mais...\033[31mTente novamente.\033[m')
        elif p > computador:
            print('Tente menos...\033[31mTente novamente.\033[m')
print(emojize(f'\033[32m:sparkles:Parabéns !! Você acertou com {cont} tentativas!!:sparkles:\033[m'))
