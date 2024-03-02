'''
Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('-=-' * 10)
print(f'{' ':>4}PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for pa in range(1, 11):
    tg = p + (pa - 1) * r  # formula de pa.
    print(f'{tg} ⇨', end=' ')
    
print('ACABOU.')
