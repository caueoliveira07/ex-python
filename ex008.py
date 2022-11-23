# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite a medida em metros: '))
print('{}m corresponde a {:.0f}mm.'.format(n,n*1000))
print('{}m corresponde a {:.0f}cm.'.format(n,n*100))
print('{}m corresponde a {:.0f}dm.'.format(n,n*10))
print('{}m corresponde a {}km.'.format(n,n/1000))
print('{}m corresponde a {}hm.'.format(n,n/100))
print('{}m corresponde a {}dam.'.format(n,n/10))
