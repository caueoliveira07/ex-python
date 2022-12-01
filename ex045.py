# Crie um programa que faça o computador jogar Jokenpô(pedra, papel e tesoura) com você.

from random import randint
from time import sleep
print('JOKENPÔ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
computador = randint(1, 3)
jogador = int(input('Faça sua escolha: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
if computador == 1 and jogador == 1:
    print('O computador escolheu Pedra.')
    print('O jogador escolheu Pedra.')
    print('Empate!')
elif computador == 1 and jogador == 2:
    print('O computador escolheu Pedra.')
    print('O jogador escolheu Papel.')
    print('Jogador ganhou!')
elif computador == 1 and jogador == 3:
    print('O computador escolheu Pedra.')
    print('O jogador escolheu Tesoura.')
    print('Computador ganhou!')
elif computador == 2 and jogador == 1:
    print('O computador escolheu Papel.')
    print('O jogador escolheu Pedra.')
    print('Computador ganhou!')
elif computador == 2 and jogador == 2:
    print('O computador escolheu Papel.')
    print('O jogador escolheu Papel.')
    print('Empate!')
elif computador == 2 and jogador == 3:
    print('O computador escolheu Papel.')
    print('O jogador escolheu Tesoura.')
    print('Jogador ganhou!')
elif computador == 3 and jogador == 1:
    print('O computador escolheu Tesoura.')
    print('O jogador escolheu Pedra.')
    print('Jogador ganhou!')
elif computador == 3 and jogador == 2:
    print('O computador escolheu Tesoura.')
    print('O jogador escolheu Papel.')
    print('Computador ganhou!')
elif computador == 3 and jogador == 3:
    print('O computador escolheu Tesoura.')
    print('O jogador escolheu Tesoura.')
    print('Empate!')
else:
    print('Jogada inválida.')
    