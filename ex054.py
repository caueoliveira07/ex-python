# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date
lista = 0
for c in range(0, 7):
    idade = int(input('Ano de nascimento: '))
    print('Idade: {}'.format(date.today().year - idade))
    if date.today().year - idade < 21:
        lista += 1
print('Não atingiu a maioridade: {}'.format(lista))
print('Atingiu a maioridade: {}'.format(7 - lista))
