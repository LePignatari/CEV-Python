nome = str(input('Digite o nome de uma cidade: ')).strip()
div = (nome.lower().split())
print('A cidade começa com SANTO?: {}'.format('santo' in div[0]))
