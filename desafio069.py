'''
Desafio 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuário quer ou não continuar. 
No final mostre: 
A) quantas pessoas tem mais de 18 anos. 
B) quantos homen foram cadastrados. 
C) quantas mulheres tem menos de 20 anos.
'''

print('\033[33m-=-' * 10)
print('     CADASTRE UMA PESSOA')
print('-=-' * 10)

idade = homens = mulheres = 0
while True:
    i = int(input('\033[m⇨ Idade: '))
    if i >= 18:  # total de pessoas com mais de 18 anos. (A)
        idade += 1
        
    s = ' '
    while s not in 'MF':    # caso digitado errado
        s = str(input('⇨ Sexo \033[35m[M/F]\033[m: ')).strip().upper()[0]
    if s == 'M':    # quantos homens foram cadastrados  (B)
        homens += 1
        
    elif s == 'F' and i < 20:  # quantas mulheres com menos de 20 anos (C)
        mulheres += 1
    print('-' * 25)
    c = ' '
    while c not in 'SN':    # caso digitado errado
        c = str(input('Quer continuar? \033[35m[S/N]\033[m: ')).strip().upper()[0]
    print('-' * 25)
    if c == 'N':
        print('\033[33m==== FIM DO PROGRAMA ====\033[m')
        print(f'Total de pessoas com mais de 18 anos: {idade}.')
        print(f'Ao todo temos {homens} homens cadastrados.')
        print(f'E temos {mulheres} mulheres com menos de 20 anos.')
        break
