# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print('O número {:.0f} é o maior'.format(maior))
print('O número {:.0f} é o menor'.format(menor))
