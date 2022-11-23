# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Quantas letras tem: {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Quantas letras tem o primeiro nome: {}'.format(len(separa[0])))

# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
