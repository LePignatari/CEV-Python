print('°°°' * 10)
print(f'{' ':>11}TABUADA')
print('°°°' * 10)
n = int(input('Digite o número da tabuada: '))
for t in range(1, 11):
    print(f'{n} x {t:2} = {n * t}')
