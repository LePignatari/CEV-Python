'''
Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import cos, tan, sin, radians
ang = float(input('Informe um ângulo: °'))
print('O ângulo {} possui: '.format(ang))
print('Cosseno: {:.2f}'.format(cos(radians(ang))))
print('Seno: {:.2f}'.format(sin(radians(ang))))
print('Tangente: {:.2f}'.format(tan(radians(ang))))
