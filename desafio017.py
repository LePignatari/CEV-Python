from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa dos comprimentos é de: {:.2f}'.format(hypot(co, ca)))
