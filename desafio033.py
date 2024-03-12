'''
Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
>>> Sem o uso de função:
'''

print('\033[32m>'*25)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('>'*25)

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if maior == menor:
    print('\033[mOs 3 valores são iguais!')
else:
    print(f'\033[mO menor valor digitado foi \033[35m{menor}')
    print(f'\033[mO maior valor digitado foi \033[35m{maior}')
