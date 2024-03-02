print('\033[33m-=-' * 5)
print('CALCULANDO A PA')
print('-=-' * 5)
p = int(input('\033[mPrimeiro termo: '))
r = int(input('Razão: '))
cont = 1
termo = p
mais = 10
total = 0
while mais != 0:
    total += mais   # inicialmente mostra os 10 primeiros termos da pa.
    while cont <= total:
        print(f'{termo} ⇨', end=' ')
        termo += r
        cont += 1
    print('\033[36mPAUSA\033[m')
    mais = int(input('Quantos termos deseja adicionar a mais? '))
print(f'Foram mostrados \033[32m{total}\033[m termos no total!')
print('\033[31mACABOU')
