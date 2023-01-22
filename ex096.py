# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {l}x{c} é de {área}m².')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)

'''# Resolução do professor


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)'''
