from random import choice
print('''Suas opções: 
(1) PEDRA
(2) PAPEL 
(3) TESOURA''')

jogador = int(input('Qual é a sua jogada?: '))
computador = choice([1, 2, 3])
print('-=-' * 10)
print(f'Computador jogou {computador}\nJogador jogou {jogador}')
print('-=-' * 10)

if jogador == computador:
    print('EMPATE!')
elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 \
        or jogador == 3 and computador == 2:
    print('VITÓRIA DO USUÁRIO!')
else:
    print('VITÓRIA DO COMPUTADOR!')
print('FIM DE JOGO.')
