# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$'))
aumento = salario + ( salario * 15 / 100)
print('O salário com 15% de aumento é R$: {:.2f}.'.format(aumento))
