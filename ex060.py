# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120.

n = int(input('Número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
n = int(input('Número: '))
print('Calculando {}! = '.format(n), end='')
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
'''
