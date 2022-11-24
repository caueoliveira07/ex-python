# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
ordem = [r1, r2, r3]
maior = max(ordem)
ordem.remove(maior)
a = ordem[0]
b = ordem[1]
if maior < a + b:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
