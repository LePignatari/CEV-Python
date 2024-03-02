from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input((f'Em que ano nasceu a {i}° pessoa: ')))
    idade = ano - nasc
    if idade >= 21:
        maior += +1
    else:
        menor += +1
print(f'''Ao todo tivemos {maior} pessoas maiores de idade
E também tivemos {menor} pessoas menores de idade!''')
