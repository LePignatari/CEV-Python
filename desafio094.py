dados = dict()
pessoas = list()
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M e F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        c = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if c in 'SN':
            break
        print('ERRO! Digite apenas S e N.')
    if c == 'N':
        break

print('-=-' * 20)
print(f'A) O grupo tem {len(pessoas)} pessoas.')
print(f'B) A média de idade é de {soma / len(pessoas):.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'[{i['nome']}]', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= (soma / len(pessoas)):
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<< ENCERRADO >>>')
