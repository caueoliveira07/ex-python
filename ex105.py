# Faça um programa que tenha uma função notas() que pode recebar várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, A maior nota, A menor nota, A média da turma e A situação (opcional). Adicione também as docstrings da função.


def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma. 
    """
    total = int()
    maior = menor = média = float()
    for n in nota:
        total += 1
        média += n
    maior = max(nota)
    menor = min(nota)
    média = média / len(nota)
    if média < 5:
        situação = str('Ruim')
    elif média < 7:
        situação = str('Razoável')
    elif média >= 7:
        situação = str('Boa')
    print('-' * 30)
    if sit == False:
        return {'total': total, 'maior': maior, 'menor': menor, 'média': média}
    else:
        return {'total': total, 'maior': maior, 'menor': menor, 'média': média, 'situação': situação}


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

'''# Resolução do professor


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma. 
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5)
print(resp)'''
