alunos = dict()

alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['Média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
