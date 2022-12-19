# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: Quantas vezes apareceu o valor 9, Em que posição foi digitado o primeiro valor 3 e Quais foram os números pares.

tupla = ()
par = ()
for c in range(0, 4):
    tupla += (int(input('Digite um número: ')),)
    if tupla[c] % 2 == 0:
        par += (tupla[c],)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if tupla.count(3) == True:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição.')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print(f'Os valores pares digitados foram {par}')

'''# Resolução do professor
num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''
