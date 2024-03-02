print('-=-'*15)
s = float(input('Digite o valor do seu salário: \033[32mR$\033[m'))
print('-=-'*15)
if s >= 1250:
    aum1 = (10 / 100) * s
    ns1 = aum1 + s
    print(f'\033[32mCom aumento de \033[31m10%\033[m \033[32mvocê receberá: R${ns1:.2f}')
else:
    aum2 = (15 / 100) * s
    ns2 = aum2 + s
    print(f'\033[32mCom aumento de \033[31m15%\033[m \033[32mvocê receberá: R${ns2:.2f}')
