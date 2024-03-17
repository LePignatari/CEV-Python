'''Desafio 081 → Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if c == 'N':
        break
valores.sort(reverse=True)
print('-=-' * 15)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
