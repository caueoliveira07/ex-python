# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for c in range(0,5):
    lista.append(float(input('Peso: ')))
print('O maior peso foi {:.1f}Kg.'.format(max(lista)))
print('O menor peso foi {:.1f}Kg.'.format(min(lista)))
