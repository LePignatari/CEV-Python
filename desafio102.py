def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-=-' * 10)
    f = 1
    for fat in range(n, 0, -1):
        f *= fat
        if show:
            print(fat, end='')
            print(' x ' if fat > 1 else ' = ', end='')
    return f


# Programa Principal
print(fatorial(5, show=True))
