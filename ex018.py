# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O seno é {:.2f}'.format(seno))
print('O cosseno é {:.2f}'.format(cosseno))
print('A tangente é {:.2f}'.format(tangente))
