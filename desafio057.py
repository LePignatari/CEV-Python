print('-=-' * 10)
sexo = str(input('Olá! Por favor, informe o seu sexo \033[32m[M/F]\033[m: ')).strip().upper()[0]
#while sexo != 'M' and sexo != 'F':    <<<< minha resolução inicial.
while sexo not in 'FM':     # enquanto a resposta não estiver em masc e fem.   <<<< resolução do professor.
    sexo = str(input('\033[31mDado incorreto\033[m, por favor informe seu sexo novamente \033[32m[M/F]\033[m: ')).strip().upper()[0]
print(f'\033[32mSexo {sexo} registrado com êxito!\033[m')
print('-=-' * 10)
