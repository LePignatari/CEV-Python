from emoji import emojize
from random import randint
print('\033[35m-=-' * 10)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
cont = computador = 0
while True:
    jogador = int(input('\033[mDiga um valor: '))
    computador = randint(0, 10)
    parimpar = ' '
    soma = jogador + computador
    while parimpar not in 'PI':
        parimpar = str(input('Par ou ímpar? \033[36m[P/I]\033[m: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}.Total de {soma}', end=' ')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')

    if parimpar == 'I':     # se o tipo for ÍMPAR
        if soma % 2 == 1:
            print(emojize(f':trophy: \033[32mVocê VENCEU!\033[m :trophy:'))
            cont += 1
        elif soma % 2 == 0:
            print(emojize(':confused_face: \033[31mVocê PERDEU!\033[m :confused_face:'))
            break
    elif parimpar == 'P':   # se o tipo for PAR
        if soma % 2 == 1:
            print(emojize(':confused_face: \033[31mVocê PERDEU!\033[m :confused_face:'))
            break
        elif soma % 2 == 0:
            print(emojize(f':trophy: \033[32mVocê VENCEU!\033[m :trophy:'))
            cont += 1
print('\033[33m-=-' * 10)
print(emojize(f'\033[31mGAME OVER!\033[m Você venceu :trophy: \033[35m{cont} vezes.:trophy:\033[33m'))
print('-=-' * 10)
