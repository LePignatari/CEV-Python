from time import sleep


def maior(*valor):
    print('-=-' * 20)
    print('Analisando os valores passados...')
    for valores in valor:
        print(valores, end=' ')
        sleep(0.5)
    print(f'- Foram informados {len(valor)} valores ao todo!')
    if len(valor) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valor)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
