from random import randint
from time import sleep

print('-=-' * 10)
print('    JOGANDO NA MEGA SENA')
print('-=-' * 10)
lista = list()  # var auxiliar.
jogos = list()
qnt = int(input('Quantos jogos você quer que eu sorteie?: '))

cont = 1
while cont <= qnt:
    while len(lista) != 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont += 1


print('-=-' * 2, f'SORTEANDO {qnt} JOGOS', '-=-' * 2)
for jogo, sorteados in enumerate(jogos):
    sleep(0.3)
    print(f'Jogo {jogo+1}: {sorteados}')
print('-=-' * 3, f'< BOA SORTE! >', '-=-' * 3)
    