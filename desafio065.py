media = soma = cont = 0
p = 'S'
lista = []
while p not in 'N':
    num = int(input('>>> Digite um número: '))
    p = str(input('Deseja continuar? \033[32m[S/N]\033[m: ')).strip().upper()[0]   # considerando a primeira letra
    cont += 1
    soma += num
    media = soma / cont
    lista += [num]
print(' ')
print(f'⇨ A \033[36mmédia\033[m entre todos os \033[33m{cont}\033[m valores foi \033[36m{media:.2f}\033[m.')
print(f'⇨ O \033[36mmaior\033[m valor foi \033[33m{max(lista)}\033[m e o \033[36mmenor\033[m foi \033[33m{min(lista)}\033[m.')
