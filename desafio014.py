'''
Desafio 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

print('='*30)
print('Conversor de Temperatura')
print('='*30)
t = float(input('Digite a temperatura em Celsius: ° '))
print('Convertido em Fahrenheit: {}°F;.'.format((t * 1.8) + 32))  # ou ((9 * t)/ 5) + 32 essa ordem de precedência tbm não precisa de ()
