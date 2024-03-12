'''
Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
>>> exercício com todas as conversões !
'''

v = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a: '.format(v))
print('{}km'.format(v / 1000))
print('{}hm'.format(v / 100))
print('{}dam'.format(v / 10))
print('{:.0f}dm'.format(v * 10))
print('{:.0f}cm'.format(v * 100))
print('{:.0f}mm'.format(v * 1000))
