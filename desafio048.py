'''
Desafio 048 - Faça um programa que calcule a soma entre todos os números ímpares, que são multiplos de três, e que se encontram no intervalo de 1 até 500.
'''

soma = 0
cont = 0
for impar in range(1, 501, 2):  # definimos os números impares
    if impar % 3 == 0:  # definimos os números multiplos de 3
        soma += impar
        cont += +1
print(f'A soma dos números foi de {soma}, encontrados em {cont} números!', end=' ')
