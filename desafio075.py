'''Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('-=-' * 15)

print(f'Você digitou os valores {num}')
print(f'A) O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'B) O valor 3 apareceu na {num.index(3) + 1} posição.')
else:
    print(f'B) O valor 3 não apareceu em nenhuma posição.')
print(f'C) Os valores pares digitados foram ', end=' ')
for n in num:   # vai mostrar somente os valores pares.
    if n % 2 == 0:
        print(n, end=' ')

