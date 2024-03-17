'''Desafio 080 → Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort() ). No final, mostre a lista ordenada na tela.'''

lista = []
for v in range(0, 5):
    num = int(input('Digite um valor: '))
    if v == 0 or num > lista[-1]:   # primeiro valor ou se o num for maior que o último valor.
        lista.append(num)           # se for um OU outro, vai adicionar no final da lista.
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):             # enquanto não ler a lista inteira.
            if num <= lista[pos]:           # se o num for menor ou igual ao número da lista na posição tal
                lista.insert(pos, num)      # ele add esse num no lugar que o número estava posicionado
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1   # contando para verificar cada elemento

print('-=-' * 15)
print(f'Os valores digitados em ordem foram {lista}')
