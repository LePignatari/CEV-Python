print('\033[36m-=-'*13)
print('Viagens de até 200Km: R$0,50 por Km.')
print('Viagens mais longas: R$0,45 por Km.')
print('-=-'*13)
d = int(input('\033[mQual a distância da viagem? '))
if d <= 200:
    print(f'Para {d}Km o valor da passagem será de \033[32mR${d * 0.50:.2f}.')
else:
    print(f"Para {d}Km o valor da passagem será de \033[32mR${d * 0.45:.2f}.")
