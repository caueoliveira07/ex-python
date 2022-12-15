# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Qual valor você quer sacar? R$'))
resultado = valor // 50
resto = valor % 50
print(f'Total de {resultado} cédulas de R$50')
resultado = resto // 20
resto = resto % 20
print(f'Total de {resultado} cédulas de R$20')
resultado = resto // 10
resto = resto % 10
print(f'Total de {resultado} cédulas de R$10')
resultado = resto // 1
print(f'Total de {resultado} cédulas de R$1')
print('Fim do programa.')

'''# Resolução do professor
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''
