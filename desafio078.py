'''Desafio 078 → Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
maior = 0
menor = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {v}: ')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]

print('-=-' * 15)
print(f'Você digitou os valores \033[32m{lista}\033[m')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for pos, v in enumerate(lista):
    if v == maior:  # se um dos números que eu coloquei for o maior ele deverá mostrar a posição que ele se encontra.
        print(f'\033[35m{pos}...', end='')
print(f'\n\033[mO menor valor digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'\033[35m{pos}...', end='')
