'''
esafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual seá o valor a ser sacado ( nmr inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1.
'''

print('\033[35m=-=' * 10)
print('     BANCO CURSO EM VÍDEO')
print('=-=' * 10)

v = float(input('\033[mQual valor você quer sacar? R$'))
n50 = n20 = n10 = n1 = cont = 0    # contadores
while True:
    if v >= 50:
        v -= 50
        n50 += 1
    elif v >= 20:
        v -= 20
        n20 += 1
    elif v >= 10:
        v -= 10
        n10 += 1
    elif v >= 1:
        v -= 1
        n1 += 1
    elif v == 0:
        break
        
print('\033[35m=-=' * 10)
print(f'\033[mTotal de {n50} cédulas de R$50')
print(f'Total de {n20} cédulas de R$20')
print(f'Total de {n10} cédulas de R$10')
print(f'Total de {n1} cédulas de R$1')
print('Volte sempre ao BANCO CURSO EM VÍDEO! Tenha um bom dia!')
print('\033[35m=-=' * 10)
