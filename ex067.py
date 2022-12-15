# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

número = 0
while número >= 0:
    número = int(input('Quer ver a tabuada de qual valor? '))
    if número < 0:
        break
    for c in range(0, 11):
        print(f'{número} x {c} = {número * c}')
print('Programa encerrado.')

'''# Resolução do professor
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print (f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''
