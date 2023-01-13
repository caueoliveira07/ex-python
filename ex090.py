# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. Se a média for 7 ou maior o aluno estará aprovado, se for menor ele estará reprovado.

dicionário = dict()
dicionário['nome'] = str(input('Nome: '))
dicionário['média'] = float(input(f'Média de {dicionário["nome"]}: '))
if dicionário['média'] >= 7:
    dicionário['situção'] = 'Aprovado'
elif dicionário['média'] >= 5 and dicionário['média'] < 7:
    dicionário['situação'] = 'Recuperação'
else:
    dicionário['situação'] = 'Reprovado'
for k, v in dicionário.items():
    print(f'{k} é igual a {v}')

'''# Resolução do professor
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')'''
