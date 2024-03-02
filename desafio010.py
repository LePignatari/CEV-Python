'''
Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (considere: R$3,27).
'''

d = float(input('Digite quanto dinheiro possui: R$'))
dolar = d / 3.27
print('Poderá comprar: US${:.2f} dólares.'.format(dolar))
