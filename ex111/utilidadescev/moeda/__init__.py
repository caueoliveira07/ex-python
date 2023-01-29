def aumentar(preço, aumento, form=True):
    r = preço + (preço / 100 * aumento)
    if form == True:
        r = moeda(r)
    return r


def diminuir(preço, diminuição, form=True):
    r = preço - (preço / 100 * diminuição)
    if form == True:
        r = moeda(r)
    return r


def dobro(preço, form=True):
    r = preço * 2
    if form == True:
        r = moeda(r)
    return r


def metade(preço, form=True):
    r = preço / 2
    if form == True:
        r = moeda(r)
    return r


def moeda(preço):
    return f'R${preço:.2f}'


def linha():
    print('-' * 30)


def resumo(preço, aumento, diminuição):
    linha()
    print(f'{"RESUMO DO VALOR":^30}')
    linha()
    print(f'{"Preço analisado: ":<15}', end='')
    print(f'{moeda(preço):>10}')
    print(f'{"Dobro do preço: ":<15}', end='')
    print(f'{dobro(preço):>10}')
    print(f'{"Metade do preço: ":<15}', end='')
    print(f'{metade(preço):>10}')
    print(f'{aumento}{"% de aumento: ":<15}', end='')
    print(f'{aumentar(preço, aumento):>10}')
    print(f'{diminuição}{"% de redução: ":<15}', end='')
    print(f'{diminuir(preço, diminuição):>10}')
    linha()


'''# Resolução do professor


def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valorreajustado, com ou sem formato.
    """
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato == False else moeda(res)

    
def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato == False else moeda(res)
    # return res if formato is False else moeda(res)
    # return res if not formato else moeda(res)
    
    
def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato == False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)'''
    