p = float(input('Digite o preço do produto: R$'))
desc = (5 / 100) * p
pf = p - desc
print('O preço do produto com 5% de desconto será de R${:.2f} reais.'.format(pf))
