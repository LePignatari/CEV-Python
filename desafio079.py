'''Desafio 079 → Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:          # se o número não estiver na lista
        valores.append(num)         # adicione
        print('Valor adicionado com sucesso...')
    else:                           # senão, ignore
        print('Valor já inserido, não vou colocar...')
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? \033[32m [S/N] \033[m: ')).strip().upper()
    if c == 'N':
        break

valores.sort()
print('-=-' * 15)
print(f'Você digitou os valores \033[33m {valores}')
