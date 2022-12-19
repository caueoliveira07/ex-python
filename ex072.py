# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while True:
        if num >= 0 and num <= 20:
            break
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    contador = 0
    for item in tupla:
        if num == contador:
            print(f'Você digitou o número {item}.')
        contador += 1
    resposta = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resposta == 'N':
        break

'''# Resolução do professor
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')'''
