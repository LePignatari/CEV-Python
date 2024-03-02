'''
Desafio 065: Crie um programa que leia varios números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar  valor.
'''

media = soma = cont = 0
p = 'S'
lista = []
while p not in 'N':
    num = int(input('>>> Digite um número: '))
    p = str(input('Deseja continuar? \033[32m[S/N]\033[m: ')).strip().upper()[0]   # considerando a primeira letra
    cont += 1
    soma += num
    media = soma / cont
    lista += [num]
print(' ')
print(f'⇨ A \033[36mmédia\033[m entre todos os \033[33m{cont}\033[m valores foi \033[36m{media:.2f}\033[m.')
print(f'⇨ O \033[36mmaior\033[m valor foi \033[33m{max(lista)}\033[m e o \033[36mmenor\033[m foi \033[33m{min(lista)}\033[m.')
