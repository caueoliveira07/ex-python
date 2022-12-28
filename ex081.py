# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: Quantos números foram digitados, A lista de  valores ordenada de forma decrescente e Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = ''
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if pergunta == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 está na posição {lista.index(5)} da lista')
else:
    print(f'O valor 5 não foi encontrado na lista!')

'''# Resolução do professor
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')'''
