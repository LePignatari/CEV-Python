from time import sleep
cores = ('\033[m',          # 0 - sem cor.
         '\033[30;42m',     # 1 - verde.
         '\033[30;46m',     # 2 - azul.
         '\033[30;41m',     # 3 - vermelho.
         '\033[30;107m')    # 4 - branco.


def titulo(mgs, cor=0):
    print(f'{cores[cor]}', end='')
    print('-' * len(mgs))
    print(mgs)
    print('-' * len(mgs))
    print(f'{cores[0]}', end='')


def sistema():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 1)
        doc = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
        if doc == 'fim':
            break
        else:
            titulo(f'Acesando o manual do comando [{doc}]', 2)
            sleep(2)
            print(cores[4], end='')
            help(doc)
            print(cores[0], end='')
    titulo('ATÉ LOGO!', 3)


sistema()
