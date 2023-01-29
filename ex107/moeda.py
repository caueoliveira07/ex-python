def aumentar(preço, aumento):
    r = preço + (preço / 100 * aumento)
    return r


def diminuir(preço, diminuição):
    r = preço - (preço / 100 * diminuição)
    return r


def dobro(preço):
    r = preço * 2
    return r


def metade(preço):
    r = preço / 2
    return r


'''# Resolução do professor


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res

    
def dobro(preço):
    res = preço * 2
    return res
    
    
def metade(preço):
    res = preço / 2
    return res'''
