# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão. 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Número inteiro: '))
print('Qual será a base de conversão?')
print('1 - Para binário.')
print('2 - Para octal.')
print('3 - Para hexadecimal.')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
