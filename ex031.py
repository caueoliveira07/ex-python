# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Distância: '))
print('{:.0f}Km'.format(km))
if km <= 200:
    preco = km * 0.50
    print('Valor cobrado: R$0.50 por Km')
else:
    preco = km * 0.45
    print('Valor cobrado: R$0.45 por Km')
print('O preço da passagem é R${:.2f}'.format(preco))
# preco = km * 0.50 if km <= 200 else km * 0.45
