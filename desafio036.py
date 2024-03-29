'''
Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
COMEÇO DO MUNDO 2
'''
print('\033[35m-=-' * 10)
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
tempo = int(input('Tempo de financiamento (anos): '))
print('-=-' * 10)

emprestimo = casa / (tempo * 12)
minimo = sal * 30 / 100  # se o salário x 30% não atingir o valor do empréstimo ele será negado !
print(f'\033[mVocê terá que pagar \033[32mR${emprestimo:.2f}\033[m por mês em \033[36m{tempo} anos\033[m até completar o valor da casa.')
if emprestimo <= minimo:
    print('\033[32mEMPRÉSTIMO LIBERADO.')
else:
    print('\033[31mEMPRÉSTIMO NEGADO.')
