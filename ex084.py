# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: Quantas pessoas foram cadastradas, Uma listagem com as pessoas mais pesadas e Uma listagem com as pessoas mais leves.

lista = []
while True:
    lista.append([str(input('Nome: ')), float(input('Peso: '))])
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
maior = 0
menor = 0
for c in lista:
    if maior < c[1]:
        maior = c[1]
    if menor == 0 or c[1] < menor:
        menor = c[1]
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in lista:
    if c[1] == maior:
        print(c[0], end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for c in lista:
    if c[1] == menor:
        print(c[0], end=' ')
print()

'''# Resolução do professor
temp = []
princ = []
maior = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end=' ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
print()'''
