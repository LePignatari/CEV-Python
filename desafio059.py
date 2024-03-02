from time import sleep
from emoji import emojize
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
maior = [n1, n2]
while op != 5:      # flag
    print('''    [1] Somar
    [2] Multiplicar
    [3] Mostrar o maior
    [4] Digitar novos números
    [5] Sair''')
    print('-=-' * 10)
    op = int(input('⇨ Qual é a sua opção?: '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
        sleep(1.3)
    elif op == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} resultará em {mult}')
        sleep(1.3)
    elif op == 3:
        print(f'O maior número entre {n1} e {n2} é {max(maior)}')
        sleep(1.3)
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        sleep(0.5)
    elif op == 5:
        print('\033[31mFinalizando...\033[m')
        sleep(1.3)
    else:
        print('Opção inválida. Tente novamente!')
    print('-=-' * 10)
sleep(0.5)
print(emojize('\033[32mFim do programa! Volte sempre!:grinning_face_with_big_eyes:'))
