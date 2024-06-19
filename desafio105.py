def notas(*n, sit=False):

    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    print('-=-' * 15)
    dados = dict()
    dados["Total"] = len(n)
    dados["Maior"] = max(n)
    dados["Menor"] = min(n)
    med = sum(n) / len(n)
    dados["Média"] = med
    if sit:
        if med <= 5:
            dados["Situação"] = 'RUIM'
        elif med >= 7:
            dados["Situação"] = 'BOA'
        else:
            dados["Situação"] = 'RAZOÁVEL'
    return dados


# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
