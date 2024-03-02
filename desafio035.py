print('°'*35)
a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
print('°'*35)
print('\033[4;36mVerificando as condições de existência...\033[m')
if a < b + c and b < a + c and c < a + b:
    print('\033[32mPodemos formar um triângulo!!.')
else:
    print('\033[31mNão podemos formar um triângulo.')
