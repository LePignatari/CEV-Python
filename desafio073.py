'''Desafio 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os  5 primeiros colocados.
B) Os últimos 4 colocados.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
OBS: adaptado para mostrar o time do Bragantino. '''

camp = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino',
        'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo',
        'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
        'Goiáis', 'Curitiba', 'América-MG')

print('\033[31m-=-' * 15)
print('   CAMPEONATO BRASILEIRO DE FUTEBOL 2023.')
print('-=-' * 15)
print(f'\033[mLista de times do Brasileirão: {camp}')
print('-=-' * 10)
print(f'Os 5 primeiros são: {camp[0:5]}')
print('-=-' * 10)
print(f'Os 4 últimos são: {camp[-4:]}')
print('-=-' * 10)
print(f'Times em ordem alfabética: {sorted(camp)}')
print('-=-' * 10)
print(f'O Bragantino está na posição {camp.index('Bragantino') + 1}!')
