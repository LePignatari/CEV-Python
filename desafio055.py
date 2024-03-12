'''
Desafio 055 - Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
>>> Usando função:
'''

maiormenor = []  # lista vazia
for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    maiormenor += [peso]   # vai adicionar os valores da variável 'peso' na lista vazia
    
print(f'O maior peso lido foi de {max(maiormenor)}')  # fazendo o camando mostrar o maior e o menor número DENTRO dessa lista.
print(f'O menor peso lido foi de {min(maiormenor)}')
