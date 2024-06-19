def voto(a):
    from datetime import date # Escopo de Importação.
    ano_atual = date.today().year
    idade = ano_atual - a
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-=-' * 10)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
