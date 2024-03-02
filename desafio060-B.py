print('\033[35m-=-' * 15)
print(f'{' ':>10}CALCULANDO O FATORIAL')
print('-=-' * 15)
num = int(input('\033[mDigite um número para calcular seu Fatorial: '))
fat = 1    # recebe 1 para fazer uma multiplicação limpa.
print(f'Contando...{num}! = ', end=' ')
for f in range(num, 0, -1):
    print(f'{f}', end=' ')
    print(' x ' if f > 1 else ' = ', end=' ')
    fat *= f
print(fat)
