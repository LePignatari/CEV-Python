print('\033[35m-=-' * 10)
print('   SEQUÊNCIA DE FIBONACCI')
print('-=-' * 10)
num = int(input('\033[m⇨ Quantos termos deseja mostrar? '))
cont = 3    # começa a contar no 3 porque ja vou mostrar o 0 ⇨ 1 no começo
anterior = 0
posterior = 1
soma = 0
print(f'{anterior} ⇨ {posterior} ⇨', end=' ')
while cont <= num:
    soma = anterior + posterior     # 0 + 1 = 1.
    anterior = posterior   # o posterior (1) se tornará o anterior.
    posterior = soma       # e o posterior agora será o resultado da soma, nesse primeiro caso, 1. >>> 1 + 1 = 2 ...
    print(f'{posterior}', end=' ⇨ ')
    cont += 1
print('\033[31mFIM')
