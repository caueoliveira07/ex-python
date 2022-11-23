# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834 unidade: 4 dezena: 3 centena: 8 milhar: 1

num = int(input('Digite um número: '))

print('Analisando o número {}'.format(num))
print('unidade: {}'.format(num // 1 % 10))
print('dezena: {}'.format(num // 10 % 10))
print('centena: {}'.format(num // 100 % 10))
print('milhar: {}'.format(num // 1000 % 10))
