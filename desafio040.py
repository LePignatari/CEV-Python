'''
Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 
→ Média abaixo de 5.0: reprovado, média entre 5.0 e 6.9: recuperação, média 7.0 ou +: aprovado.
'''

print('-=-'*5)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('-=-'*5)
m = (n1 + n2) / 2
print(f'Sua média foi de {m:.1f}!.')
if m < 5.0:
    print('\033[31mREPROVADO.')
elif m <= 6.9:
    print('\033[36mRECUPERAÇÃO.')
elif m >= 7.0:
    print('\033[32mAPROVADO.')
