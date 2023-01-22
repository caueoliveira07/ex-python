# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=False):
    """
    -> Calcule o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    resultado = 1
    for c in range(n, 0, -1):
        resultado *= c
    print('-' * 30)
    if show == False:
        return resultado
    else:
        for c in range(n, 0, -1):
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
        return resultado


print(fatorial(5))
help(fatorial)

'''# Resolução do professor


def fatorial(n, show=False):
    """
    -> Calcule o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=''
            )
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5))'''
