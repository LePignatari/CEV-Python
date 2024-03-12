'''Desafio 076: Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência.
No Final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for prod in range(0, len(listagem)):
    if prod % 2 == 0:   # todos os produtos ficaram de um lado (esquerda)
        print(f'{listagem[prod]:.<30}', end='')
    else:   # todos os preços ficaram de um lado (direito)
        print(f'R${listagem[prod]:>7.2f}')
print('-' * 40)
