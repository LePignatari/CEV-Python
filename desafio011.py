'''
Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a sua quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m2.
'''

v1 = float(input('Digite a largura da sua parede em metros: '))
v2 = float(input('Digite a altura da sua parede em metros: '))
a = v1 * v2
qt = a / 2
print('Para pintar uma área de {}m2, você precisa de {} litros de tinta para pintá-la'.format(a, qt))
