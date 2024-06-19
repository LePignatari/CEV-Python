def leiaInt(num):
    print('-=-' * 15)
    while True:
        lendo = input(num)
        if lendo.isnumeric():
            return lendo
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
