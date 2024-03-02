'''
Desafio 022:  Crie um programa que leia o nome completo de uma pessoa e mostre:          
→ O nome com todos as letras maiúsculas.   
→ O nome com todas as letras minúsculas.       
→ Quantas letras ao todo (sem considerar espaços). 
→ Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
div = nome.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(div[0], len(div[0])))
print('Seu nome possui {} letras ao todo !.'.format(len(nome) - nome.count(' ')))
