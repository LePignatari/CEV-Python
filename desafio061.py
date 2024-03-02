print('\033[33m-=-' * 5)
print('CALCULANDO A PA')
print('-=-' * 5)
termo = int(input('\033[mPrimeiro termo: '))
r = int(input('Razão: '))
p = termo
cont = 1
while cont <= 10:
    print(f'{p} ⇨', end=' ')
    p += r         # vai fazer a soma ex: primeiro termo = 5 e razão = 3 == 5 (5+3) ⇨ 8 (8+3) ⇨ 11... até o 10° termo.
    cont += 1      # contagem até o 10° termo.
print('\033[31mACABOU')
