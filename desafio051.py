print('-=-' * 10)
print(f'{' ':>4}PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for pa in range(1, 11):
    tg = p + (pa - 1) * r  # formula de pa.
    print(f'{tg} ⇨', end=' ')
print('ACABOU.')
