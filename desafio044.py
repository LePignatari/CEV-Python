'''
Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
→ Á vista dinheiro/cheque: 10% de desconto
→ Á vista cartão: 5% de desconto
→ Em até 2x no cartão: preço normal
→ 3x ou mais no cartão: 20% de juros.
'''

print('\033[36m-' * 30)
print(f'{' ':^5}LOJA CURSO EM VÍDEO')
print(f'-' * 30)
valor_produto = float(input('Preço da compra (R$): '))      # valor do produto
print('\033[33m-=-' * 15)

print('FORMAS DE PAGAMENTO: ')
print('''1) Á vista dinheiro/cheque (10% de desconto).
2) Á vista no cartão (5% de desconto).
3) Em até 2x no cartão (sem juros).
4) Em 3x ou mais no cartão (20% de juros).''')
print('-=-' * 15)

pagamento = int(input('\033[mQual a forma de pagamento?: '))     # condição de pagamento
if pagamento == 1:
    total = valor_produto - (valor_produto * 10 / 100)
elif pagamento == 2:
    total = valor_produto - (valor_produto * 5 / 100)
elif pagamento == 3:
    total = valor_produto / 2
    print(f'Sua compra parcelada em 2x será de R${total:.2f} \033[32mSEM JUROS\033[m.')
elif pagamento == 4:
    total = valor_produto + (valor_produto * 20 / 100)
    p = int(input('Em quantas vezes deseja parcelar?: '))
    parcela = total / p
    print(f'Sua compra parcelada em {p}x será de R${parcela:.2f} \033[31mCOM JUROS\033[m.')
else:
    total = 0
    print('\033[31mESTÁ OPÇÃO NÃO É VÁLIDA, TENTE NOVAMENTE.\033[m')
    
print(f'Sua compra de R${valor_produto:.2f} vai custar \033[32mR${total:.2f}.')
print(' ')
print('\033[35m-=-' * 15)
print(f'{' ':^5}OBRIGADO POR COMPRAR, VOLTE SEMPRE!')
print('-=-' * 15)
