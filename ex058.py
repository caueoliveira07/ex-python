# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"  em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessáris para vencer.

from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
print('Tente adivinhar o número escolhido pelo computador...')
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
