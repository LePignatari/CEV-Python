'''
Desafio 029: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''

print('-'*40)
print('\033[4;33mVELOCIDADE PERMITIDA:\033[m abaixo de 80km/h')
print('\033[4;31mMulta de R$7,00 por Km excedente.\033[m')
print('-'*40)

v = float(input('Digite a velocidade do carro: '))
m = (v - 80) * 7

if v <= 80:
    print('Você atendeu os limites de velocidade.')
    print('\033[32mO seu carro não levou multa!\033[mTenha um \033[36mbom dia.\033[m')
else:
   print('\033[31mO seu carro ultrapassou 80km/h.')
   print(f'Você foi multado em \033[32mR${m:.2f}\033[m. Dirija com segurança!')
