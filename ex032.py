# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Ano: '))
if ano % 4 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
