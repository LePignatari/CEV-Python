def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
