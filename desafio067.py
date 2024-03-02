'''
Desafio 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitada pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
'''

while True:
    n = int(input('Qual valor deseja ver a tabuada?: '))
    cont = 1
    print('-=-' * 10)
    if n < 0:   # já verifica se o número é negativo.
        print('\033[33mPROGRAMA TABUADA ENCERRADO.\033[32mVolte Sempre!')
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n * cont}')
        cont += 1
    print('-=-' * 10)
