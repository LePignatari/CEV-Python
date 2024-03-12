'''
Desafio 066: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles ( desconsiderando o flag).
'''

n = s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n  # não considera o flag na soma
    c += 1  # não considera o flag na contagem
print(f'Foram digitados {c} números, sendo sua soma {s}!')
