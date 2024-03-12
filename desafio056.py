'''
Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
→ A média de idade do grupo
→ Qual é o nome do homem mais velho
→ Quantas mulheres têm menos de 20 anos.
'''

m = 0
cont = 0
mulheres = []
velho = ''
velho_idade = 0
for p in range(1, 5):
    print(f'---- {p}° PESSOA ----')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).lower().strip()
    m += i / 4                         # média.
    if p == 1 and s == 'm':            # atribuindo o mais velho e o nome do mais velho na primeira opção.
        velho = n
        velho_idade = i
    if s == 'm' and i > velho_idade:   # caso tenho alguém mais velho, esse mais velho passa a atribuir os valores nome e idade.
        velho = n
        velho_idade = i
    if s == 'f':                       # sendo mulher:
        mulheres += [i]                # atribuindo a idade das mulheres na lista
        if i < 20:                     # analisando quais possuem menos de 20 anos
            cont += 1                  # caso encontrado é adicionado na contagem.

print('-=-' * 15)
print(f'A média de idade do grupo é de {m} anos.')
print(f'O homem mais velho tem {velho_idade} anos e se chama {velho}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')
print('-=-' * 15)
