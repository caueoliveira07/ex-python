# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos irá pagar? ' ))
excedente = 30 / 100 * sal
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação > excedente:
    print('Você não pode fazer um empréstimo.')
else:
    print('Você pode fazer um empréstimo.')
