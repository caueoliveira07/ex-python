# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('Número {}.'.format(n))
print('O dobro é {}.'.format((n*2)))
print('O triplo é {}.'.format((n*3)))
print('A raiz quadrada é {:.2f}.'.format((n**(1/2))))
