# Aprimore o desafio anterior, mostrando no final: A soma de todos os valores pares digitados, A soma dos valores da terceira coluna e O maior valor da segunda linha.

lista = [[], [], []]
pares = 0
for c in range(0, 3):
    lista[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    lista[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    lista[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
for c in range(0, 3):
    for c in lista[c]:
        if c % 2 == 0:
            pares += c
print(f'[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]')
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {lista[0][2] + lista[1][2] + lista[2][2]}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')

'''# Resolução do professor
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')'''
