'''
Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
>>> Utilizei função:
'''

print('\033[35m|'*25)
p = int(input('Digite o primeiro valor: '))
s = int(input('Digite o segundo valor: '))
t = int(input('Digite o terceiro valor: '))
print('|'*25)
num = [p, s, t]
print(f'\033[4;33mO maior número é:\033[m \033[32m{max(num)}') # essa função já me entrega qual é o maior número.
print(f'\033[4;33mO menor número é:\033[m \033[32m{min(num)}') # e essa o menor número.
