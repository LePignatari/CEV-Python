'''
Desafio 055 - Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
>>> Sem função, usando lógica:
'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:             # se for a primeira pessoa ele ja atribui como maior e menor.
        menor = peso
        maior = peso
    else:                  # senão, se for colocado um valor maior ele passa a ser o maior.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print(f'O maior peso foi de {maior}')
print(f'O menor peso foi de {menor}')
