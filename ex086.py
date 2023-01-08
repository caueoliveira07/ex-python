# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista = [[], [], []]
for c in range(0, 3):
    lista[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    lista[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    lista[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print(f'[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]')

'''# Resolução do professor
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''