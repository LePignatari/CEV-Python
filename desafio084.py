geral = list()
aux = list()
mai = men = 0
while True:
    print('-=-' * 10)
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))

    if len(geral) == 0:
        mai = men = aux[1]
    else:
        if aux[1] > mai:
            mai = aux[1]
        if aux[1] < men:
            men = aux[1]

    geral.append(aux[:])
    aux.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
print('-=-' * 20)
print(f'Ao todo, você cadastrou {len(geral)} pessoas.')
print(f'O maior peso foi de {mai:.1f}Kg. Peso de ', end='')
for p in geral:                 # maior peso
    if p[1] == mai:             # se o peso estiver no maior, mostre o nome do dono desse peso
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {men:.1f}Kg. Peso de ', end='')
for p in geral:                 # menor peso
    if p[1] == men:             # se o peso estiver no menor, mostre o nome do dono desse peso
        print(f'[{p[0]}] ', end='')
