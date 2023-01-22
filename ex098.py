# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a) De 1 até 10, de 1 em 1, b) De 10 até 0, de 2 em 2 e c) Uma contagem personalizada.


def mensagem(i, f, p1, p2):
    print('-' * 30)
    print(f'Contagem de {i} até {f} de {p1} em {p2}')


def contador(início, fim, passo):
    if início < fim:
        if passo == 0:
            passo = 1
            mensagem(início, fim, passo, passo)
            fim += 1
        if passo < 0:
            passo = passo - passo - passo
            mensagem(início, fim, passo, passo)
            fim += passo
        if passo > 0:
            mensagem(início, fim, passo, passo)
            fim += 1
    if início > fim:
        if passo == 0:
            passo = 1
            mensagem(início, fim, passo, passo)
            passo = -1
            fim -= 1
        if passo < 0  and fim == 0:
            p = passo - passo - passo
            mensagem(início, fim, p, p)
            fim -= 1
        if passo < 0  and fim > 0:
            p = passo - passo - passo
            mensagem(início, fim, p, p)
            fim -= 1
        if passo > 0:
            mensagem(início, fim, passo, passo)
            passo = passo - passo - passo
            fim -= 1
    for i in range(início, fim, passo):
        print(i, end=' ')
    print('Fim!')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

'''# Resolução do professor
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''
