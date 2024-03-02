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
