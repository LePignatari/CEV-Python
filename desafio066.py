n = s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n  # não considera o flag na soma
    c += 1  # não considera o flag na contagem
print(f'Foram digitados {c} números, sendo sua soma {s}!')
