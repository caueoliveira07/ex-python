# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    teste = int(input('Digite um valor: '))
    if teste not in lista:
        lista.append(teste)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    if continuar == 'N':
        lista.sort()
        break
print(f'Você digitou os valores {lista}')

# Resolução do professor
'''números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')'''
