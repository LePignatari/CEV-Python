dados = dict()
gols = list()
jogadores = list()

while True:
    gols.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    qnt = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for i in range(qnt):
        gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    while True:
        c = str(input('Quer continuar? [S/N] ')).strip().upper()
        if c in 'SN':
            break
        print('ERRO! Por favor digite apenas S/N.')
    if c == 'N':
        break
print('-=-' * 20)
print('cod ', end='')
for k in dados.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end='')
    print()
print('-' * 40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if n == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    if n >= len(jogadores):
        print(f'ERRO! Não temos nenhum jogador com o código {n}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}')
        for pos, v in enumerate(jogadores[n]["gols"]):
            print(f'  No jogo {pos+1} fez {v} gols.')
    print('-' * 40)
