'''
Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

v = float(input('Digite um valor em Metros: '))
cm = v * 100
mm = v * 1000
print('{}m é igual a {:.0f}cm e é igual a {:.0f}mm'.format(v, cm, mm))
