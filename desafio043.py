'''
Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
→ Abaixo de 18.5: abaixo do peso
→ Entre 18.5 e 25: peso ideal
→ 25 até 30: sobrepeso
→ 30 até 40: obesidade
→ Acima de 40: obesidade mórbida.
'''

print('v' * 15)
print('CÁLCULO DE IMC')
print('^' * 15)

a = float(input('Informe sua altura (m): '))
p = float(input('Informe seu peso (kg): '))
imc = p / (a ** 2)

print(f'\033[32mIMC:\033[m {imc:.2f}')

if imc < 18.5:
    print('\033[31mAbaixo do peso.')
elif imc <= 25:
    print('\033[32mPeso normal.')
elif imc <= 30:
    print('\033[33mSobrepeso.')
elif imc <= 40:
    print('\033[31mObesidade.')
else:
    print('\033[30;41mObesidade mórbida.\033[m')
