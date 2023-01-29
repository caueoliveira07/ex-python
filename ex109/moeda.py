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
    return f'R${preço:.2f}'.replace('.', ',')


'''# Resolução do professor


def aumentar(preço=0, taxa=0, formato=False):
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
    '''