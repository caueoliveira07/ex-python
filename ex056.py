# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, Qual é o nome do homem mais velho e Quantas mulheres têm menos de 20 anos.

média = 0
homem = 0
velho = 0
mulher = 0
for contador in range(0, 4):
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    média += i
    s = str(input('Sexo (M/F): ')).strip().upper()
    if s == 'M' and i > velho:
        homem = n
        velho = i
    if s =='F' and i < 20:
        mulher += 1
somaidade = média / 4
print('A média de idade do grupe é {}'.format(somaidade))
print('O nome do homem mais velho é {}'.format(homem))
if mulher == 1:
    print('{} mulher tem menos de 20 anos'.format(mulher))
else:
    print('{} mulheres tem menos de 20 anos'.format(mulher))
    