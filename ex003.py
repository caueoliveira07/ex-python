# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))

# Maneira sem o .format
# print('A soma entre',n1,'e',n2,'é',s)
