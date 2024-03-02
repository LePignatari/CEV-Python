print('-=-'*5)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('-=-'*5)
m = (n1 + n2) / 2
print(f'Sua média foi de {m:.1f}!.')
if m < 5.0:
    print('\033[31mREPROVADO.')
elif m <= 6.9:
    print('\033[36mRECUPERAÇÃO.')
elif m >= 7.0:
    print('\033[32mAPROVADO.')
