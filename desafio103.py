def ficha(jog="<desconhecido>", gols=0):
    print(f"O jogador {jog} fez {gols} gol(s) no campeonato.")


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gols=0)
else:
    ficha(n, g)
