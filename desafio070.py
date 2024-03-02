'''
Desafio 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre: 
A) qual é o total gasto na compra. 
B) quantos produtos custam mais de R$1000. 
C) qual é o nome do produto mais barato.
'''

print('\033[35m=-=' * 10)
print('     LOJA CURSO EM VÍDEO')
print('=-=' * 10)

mais = soma = cont = menor = nome_barato = 0
while True:
    p = str(input('\033[m⇨ Nome do produto: ')).strip().capitalize()
    v = float(input('⇨ Preço: R$'))
    cont += 1
    soma += v               # somando o valor de todos (A)
    if v > 1000:            # quantos acima de R$1000   (B)
        mais += 1
        
    if cont == 1 or menor > v:   # classifica o primeiro como o mais barato, verifica se esse valor vai mudar
        menor = v
        nome_barato = p
    c = ' '
    while c not in 'SN':    # digitação errada
        c = str(input('Quer continuar? \033[35m[S/N]\033[m: ')).strip().upper()[0]
    if c == 'N':
        print('-=-' * 10)
        print('-----\033[31m FIM DO PROGRAMA \033[m-----')
        print(f'O total da compra foi \033[32mR${soma:.2f}\033[m')
        print(f'Temos \033[32m{mais} produtos\033[m custando mais de R$1000.00')
        print(f'O produto mais barato foi {nome_barato} que custa R${menor:.2f}')
        print(f'Foram registrados \033[36m{cont} produtos!\033[m')
        print('-=-' * 10)
        break
