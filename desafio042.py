'''
Desafio 042: Refaça o desafio 035
(Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.)
dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
→ Equilátero: todos os lados iguais 
→ Isósceles: dois lados iguais 
→ Escaleno: todos os lados diferentes.
'''

print('-=-' * 10)
print('ANALISANDO O TRIÂNGULO')
r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))
print('-=-' * 10)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mPodemos\033[m formar um triângulo!')
    if r1 == r2 == r3:
        print('Sendo um triângulo \033[35mEQUILÁTERO\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Sendo um triângulo \033[35mISÓSCELES\033[m.')
    else:
        print('Sendo um triângulo \033[35mESCALENO\033[m.')
else:
    print('\033[31mNão podemos formar um triângulo.')
