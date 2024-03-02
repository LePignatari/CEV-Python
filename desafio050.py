'''
Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

print('-=-' * 10)
print(F'{' ':>8}TERMOS PARES')
print('-=-' * 10)

cont = 0
soma = 0
for p in range(1, 7):
    n = int(input(f'{p}) Digite um número: '))
    if n % 2 == 1:
        soma += n
        cont += +1
        
print(f'A soma dos {cont} termos pares foi de: {soma}')
