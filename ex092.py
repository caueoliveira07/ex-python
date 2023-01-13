# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (se aposenta depois de 35 anos).

from datetime import date
dicionário = {'nome': str(input('Nome: ')), 'nascimento': int(input('Ano de Nascimento: ')), 'idade': 0, 'carteira': int(input('Carteira de Trabalho (0 não tem): '))}
dicionário['idade'] = date.today().year - dicionário['nascimento']
if dicionário['carteira'] != 0:
    dicionário['contratação'] = int(input('Ano de Contratação: '))
    dicionário['salário'] = float(input('Salário: R$'))
    dicionário['aposentadoria'] = dicionário['contratação'] - dicionário['nascimento'] + 35
del dicionário['nascimento']
for k, v in dicionário.items():
    print(f'{k} tem o valor {v}')

'''# Resolução do professor
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$')) 
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    print('-=' * 30)
    for k, v in dados.items():
        print(f'    - {k} tem o valor {v}')'''
