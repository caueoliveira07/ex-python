# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = total = 0
while contador == 0:
    jogador = int(input('Diga um valor: '))
    resposta = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    computador = randint(1, 10)
    if (jogador + computador) % 2 == 0 and resposta == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} deu PAR.')
        print('Você venceu!')
    elif (jogador + computador) % 2 == 1 and resposta == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} deu ÍMPAR.')
        print('Você venceu!')
    elif (jogador + computador) % 2 == 0 and resposta == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} deu PAR.')
        print('Você perdeu!')
        print(f'Fim de jogo. Você venceu {total} vezes.')
        break
    elif (jogador + computador) % 2 == 1 and resposta == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} deu íMPAR.')
        print('Você perdeu!')
        print(f'Fim de jogo. Você venceu {total} vezes.')
        break
    total += 1

'''# Resolução do professor
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')'''
