'''
Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
'''

p = float(input('Digite o preço do produto: R$'))
desc = (5 / 100) * p
pf = p - desc
print('O preço do produto com 5% de desconto será de R${:.2f} reais.'.format(pf))
