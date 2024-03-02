print('='*30)
print('ALUGUEL DE CARROS!')
print('='*30)

print(' R$60 POR DIA \n R$0,15 POR KM RODADO')

print('='*30)
d = int(input('Para quantos dias foram alugados?: '))
km = float(input('Quantos Km foram rodados?: '))
v = d * 60
v2 = km * 0.15
print('O total a pagar é de: R$ {:.2f}'.format(v + v2))
