# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço: R$'))
desconto = 5/100*preco
print('R$: {:.2f} com desconto de 5% é R$: {:.2f}.'.format(preco,preco-desconto))
