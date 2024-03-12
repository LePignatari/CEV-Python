'''
Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep
from emoji import emojize
lista = [emojize('Pedra :raised_fist:'), emojize('Papel :raised_hand:'), emojize('Tesoura :victory_hand:')]
computador = randint(0, 2)
print('\033[35m°°°' * 15)
print(f'{' ':>5}SEJA BEM-VINDO AO JOGO DE JOKENPÔ')
print('°°°' * 15)

print('''\033[mSuas opções:
\033[36m[ 0 ]\033[m Pedra
\033[36m[ 1 ]\033[m Papel
\033[36m[ 2 ]\033[m Tesoura''')
jogador = int(input('>>> Escolha uma jogada: '))

print('')
print(f'{' ':>11}\033[33mJO', end='')
sleep(1)
print('\033[35mKEN', end='')
sleep(1)
print('\033[36mPÔ!\033[m')
sleep(0.7)

print(emojize(f'{' ':>11} :raised_fist::raised_hand::victory_hand:'))
print('\033[33m-=-' * 10)
print(f'\033[mJogada do usuário: {lista[jogador]}')
print(f'Jogada do computador: {lista[computador]}')
print('\033[33m-=-' * 10, '\033[m')
print('Sendo assim...', end='')
sleep(0.7)

if computador == 0:  # computador jogou pedra.
    if jogador == 0:
        print(emojize('\033[33mEMPATE!:handshake:'))
    elif jogador == 1:
        print(emojize('\033[32mUSUÁRIO VENCE!:trophy:'))
    elif jogador == 2:
        print(emojize('\033[31mCOMPUTADOR VENCE!:trophy:'))
    else:
        print('\033[31mJOGADA INVÁLIDA.')
elif computador == 1:  # computador jogou papel.
    if jogador == 1:
        print(emojize('\033[33mEMPATE!:handshake:'))
    elif jogador == 0:
        print(emojize('\033[31mCOMPUTADOR VENCE!:trophy:'))
    elif jogador == 2:
        print(emojize('\033[32mUSUÁRIO VENCE!:trophy:'))
    else:
        print('\033[31mJOGADA INVÁLIDA.')
elif computador == 2:  # computador joga tesoura.
    if jogador == 2:
        print(emojize('\033[33mEMPATE!:handshake:'))
    elif jogador == 0:
        print(emojize('\033[32mUSUÁRIO VENCE!:trophy:'))
    elif jogador == 1:
        print(emojize('\033[31mCOMPUTADOR VENCE!:trophy:'))
    else:
        print('\033[31mJOGADA INVÁLIDA.')
        
print(' ')
print(emojize(f'''{' ':>6}\033[32m:alien_monster:FIM DE JOGO!:alien_monster:
{' ':>3}:grinning_face_with_smiling_eyes:OBRIGADO POR JOGAR!:grinning_face_with_smiling_eyes:'''))
