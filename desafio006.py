'''
Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

num = int(input('Digite um número: '))
d = num * 2
t = num * 3
rq = num ** (1/2)
print(' O seu dobro é de {},\n Seu triplo é de {}\n E sua raiz quadrada é de {:.2f}'.format(d, t, rq))
