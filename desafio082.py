'''Desafio 082 → Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores ímpares  e pares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

valores = []
pares = []
impares = []

while True:
    num = (int(input('Digite um valor: ')))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break

print('-=-' * 15)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
