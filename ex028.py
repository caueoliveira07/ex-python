# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
randnum = randint(0, 5)
print('Tente adivinhar o número de 0 a 5')
num = int(input('Digite o número: '))
print('Processando...')
sleep(1)
if randnum == num:
    print('Parabéns. Você acertou!')
else:
    print('Infelizmente você errou!')
print('O seu número foi {}.'.format(num))
print('O número sorteado foi {}.'.format(randnum))
