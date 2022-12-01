# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. Á vista dinheiro/cheque: 10% de desconto, Á vista no cartão: 5% de desconto, Em até 2x no cartão: preço normal e 3x ou mais no cartão: 20% de juros.

preco = float(input('Qual o preço das compras? R$'))
print('Escolha uma forma de pagamento...')
print('1 - Á vista dinheiro/cheque: 10% de desconto.')
print('2 - Á vista no cartão: 5% de desconto.')
print('3 - Em até 2x no cartão: preço normal.')
print('4 - 3x ou mais no cartão: 20% de juros.')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (10 / 100 * preco)
    print('Valor a ser pago: R${:.2f}'.format(total))
elif opcao == 2:
    total = preco - (5 / 100 * preco)
    print('Valor a ser pago: R${:.2f}'.format(total))
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('A compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (20 / 100 * preco)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(preco, total))
