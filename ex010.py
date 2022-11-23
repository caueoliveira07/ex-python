# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

carteira = float(input('Digite o valor: R$'))
dolar = carteira/3.27
iene = carteira/0.0384
euro = carteira/5.51
print('Com R${:.2f} você pode comprar US${:.2f} (Dólar)'.format(carteira,dolar))
print('Com R${:.2f} você pode comprar ¥{:.2f} (Iene)'.format(carteira,iene))
print('Com R${:.2f} você pode comprar €{:.2f} (Euro)'.format(carteira,euro))
