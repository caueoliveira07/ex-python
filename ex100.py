# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint


def sorteia():
    números.append(randint(1, 10))


def somaPar():
    soma = int()
    for i in números:
        if i % 2 == 0:
            soma += i
    print(soma)


números = list()
soma = int()
print('Sorteando 5 valores da lista: ', end='')
for i in range(0, 5):
    sorteia()
    print(números[i], end=' ')
print()
print('Pronto!')
print(f'Somando os valores pares de {números}, temos ', end='')
somaPar()

'''# Resolução do professor
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
números = list()
sorteia(números)
somaPar(números)'''
