s = float(input('Digite o valor atual do seu salário: R$'))
aum = (15 / 100) * s
ns = s + aum
print('Com um aumento salárial de 15% agora você ganhará R${:.2f}!'.format(ns))
