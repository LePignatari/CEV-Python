n = int(input('Digite um número: '))
print('-=-' * 10)
print('''ESCOLHA A BASE DE CONVERSÃO:
[1] Binário.
[2] Octal. 
[3] Hexadecimal.''')
print('-=-' * 10)
esc = int(input('Sua opção: '))
if esc == 1:
    print(f'Convertendo {n} para Binário >>> O resultado será: {bin(n)[2:]}')
elif esc == 2:
    print(f'Convertendo {n} para Octal >>> O resultado será: {oct(n)[2:]}')
elif esc == 3:
    print(f'Convertendo {n} para Hexadecimal >>> O resultado será: {hex(n)[2:]}')
else:
    print('NÃO TEMOS ESSA OPÇÃO, TENTE NOVAMENTE.')
