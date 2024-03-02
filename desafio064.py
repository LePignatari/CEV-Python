num = int(input('⇨ Digite um valor [ou \033[31m999\033[m para parar]: '))
cont = 0
soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('⇨ Digite um valor [ou \033[31m999\033[m para parar]: '))     # o flag não vai ser somado porque se ele for 999 ele vai sair laço.
print(f'Foram digitados {cont} números e a soma deles foi de {soma}.')
