# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

'''
c = 0
total = 0
soma = 0
while c < 1:
    numero = int(input('Número: '))
    if numero == 999:
        c = 1
    else:
        soma += numero
        total += 1
print('Números digitados: {}'.format(total))
print('Soma dos números digitados: {}'.format(soma))
'''
