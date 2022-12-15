# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: qual é o total gasto na compra, quantos produtos custam mais de R$1000,00 e qual é o nome do produto mais barato.

c = total = mais = nomemenor = contador = 0
while c == 0:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total += preço
    contador += 1
    if preço > 1000:
        mais += 1
    if contador == 1:
        menor = preço
        nomemenor = nome
    else:
        if preço < menor:
            menor = preço
            nomemenor = nome
    continuar= str(input('Quer continuar? ')).upper()
    if continuar == 'N':
        c = 1
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} que custa {menor:.2f}')

'''total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float (input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp =str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')'''
