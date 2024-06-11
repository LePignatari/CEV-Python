matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:   # A) soma dos valores pares.
            pares += matriz[l][c]
        if c == 2:                  # B) soma dos valores da terceira coluna.
            soma_coluna += matriz[l][c]

print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=-' * 20)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')    # C) maior valor da segunda linha
print('-=-' * 20)
