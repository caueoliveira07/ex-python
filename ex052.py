# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
lista = []
for c in range(2, n):
    lista.append(n % c)
if n == 1 or 0 in lista:
    print('O número {} não é primo.'.format(n))
else:
    print('O número {} é primo.'.format(n))
