'''Desafio 083 → Crie um programa onde o usuário digite um expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input('Digite a expressão: '))
simb = []
for s in exp:
    if s == '(':
        simb.append('(')
    elif s == ')':
        if len(simb) > 0:
            simb.pop()
        else:
            simb.append(')')
            break
if len(simb) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
