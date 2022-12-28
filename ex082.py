# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
ímpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = ''
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if pergunta == 'N':
        break
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
    else:
        ímpar.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')

'''# Resolução do professor
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')'''
