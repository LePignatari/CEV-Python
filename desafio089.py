lista = list()
nome = list()
notas = list()
media = list()
while True:
    nome.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media.append((n1 + n2) / 2)
    notas.append(n1)
    notas.append(n2)
    nome.append(notas[:])
    notas.clear()
    nome.append(media[:])
    media.clear()
    lista.append(nome[:])
    nome.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break

print('-=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for pos, i in enumerate(lista):
    print(f'{pos:<4}{i[0]:<10}{i[2][0]:>8.1f}')
print('-' * 30)

n = 0
while n != 999:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for pos, i in enumerate(lista):
        if n == pos:
            print(f'Notas de {i[0]} são {i[1]}')
            print('-' * 30)
print('\033[32mFINALIZANDO...', end='')
print('\n<<< VOLTE SEMPRE! >>>')
