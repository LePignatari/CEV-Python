'''
Desafio 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = str(input('Escreva seu nome completo:')).strip()
n = nome.split()

print('Muito prazer em te conhecer!')
print(f'\033[35mPrimeiro nome:\033[m {n[0]}')
print(f'\033[35mÚltimo nome:\033[m {n[-1]}')  # print('Último nome: {}'.format(n[len(n)-1]))
# o [-1] pode ser utilizado para se referir ao último objeto de uma lista.
