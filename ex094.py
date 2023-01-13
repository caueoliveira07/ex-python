# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: Quantas pessoas foram cadastradas, A média de idade do grupo, Uma lista com todos as mulheres e Uma lista com todas as pessoas com idade acima da média.

lista = list()
média = float()
while True:
    dicionário = {'nome': str(input('Nome: ')), 'sexo': str(input('Sexo: [M/F] ')).upper()[0], 'idade': int(input('Idade: '))}
    lista.append(dicionário.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-' * 50)
print(f'O grupo tem {len(lista)} pessoas.')
for d in lista:
    média += d['idade']
média = média / len(lista)
print(f'A média de idade é de {média} anos.')
print('As mulheres cadastradas foram: ', end='')
for d in lista:
    if d['sexo'] == 'F':
        print(d['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média:')
for d in lista:
    if d['idade'] > média:
        print(f'nome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]}')

'''# Resolução do professor
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estáo acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''
