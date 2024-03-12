'''
Desafio 005: Faça um programa que leia o número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

num = int(input('Digite um número inteiro: '))
suc = num + 1
ant = num - 1
print('O sucessor de {} é {} e seu antecessor é {}!'.format(num, suc, ant))
