# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar, Se é a hora de se alistar ou Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('Você é do sexo masculino ou feminino?')
print('1 - Masculino')
print('2 - Feminino')
sexo = int(input('Escolha uma das opções acima: '))
if sexo == 1:
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente.')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 2:
    print('Você não precisa se alistar.')
else:
    print('Opção inválida. Tente novamente.')
