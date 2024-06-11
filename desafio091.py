from random import randint
from time import sleep

jogadores = dict()
c = 1

print('Valores sorteados: ')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
print('-=-' * 10)
print('== RANKING DOS JOGADORES == ')
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for k, v in ranking.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c += 1
