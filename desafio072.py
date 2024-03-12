'''Desafio 072: Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostrá-lo por extenso.
Aprimorado com “continuar? S/N”.'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
print('\033[33mNÚMEROS EM EXTENSO')
print('-=-' * 10)

while True:
    continuar = 'S'
    while continuar not in 'N':
        while True:
            num = int(input('\033[mDigite um número entre 0 e 20: '))
            if 0 <= num <= 20:  # se o número estiver entre 0 e 20 pare, se não, tente novamente.
                break
            print('Tente novamente.', end=' ')
        print(f'Você digitou o número \033[35m{extenso[num]}\033[m')
        continuar = str(input('Deseja continuar? \033[32m[S/N]\033[m: ')).strip().upper()
    break
print('\033[33m-=-' * 10)
print('PROGRAMA FINALIZADO COM SUCESSO!')
