'''
Desafio 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem: 
→ O primeiro valor é o maior, O segundo valor é o maior, Não existe valor maior, os dois são iguais.
'''

print('-=-'*10)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-=-'*10)
print('Analisando os valores...')

if n1 > n2:
    print('O \033[35mprimeiro valor\033[m é \033[32mMAIOR\033[m!')
elif n2 > n1:
    print('O \033[35msegundo valor\033[m é o \033[32mMAIOR\033[m!')
else:
    print('\033[35mNão existe valor maior\033[m, os dois são \033[32miguais\033[m!')
