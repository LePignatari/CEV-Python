dados = dict()
gols = list()

dados['nome'] = str(input('Nome do Jogador: '))
qnt = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
for i in range(qnt):
    gols.append(int(input(f'Quantos gols na partida {i}?: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('-=-' * 20)
print(dados)
print('-=-' * 20)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 20)

print(f'O jogador {dados['nome']} jogou {qnt} partidas.')
for pos, v in enumerate(gols):
    print(f'=> Na partida {pos}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
