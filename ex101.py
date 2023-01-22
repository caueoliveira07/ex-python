# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(n):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - n
    if idade < 16:
        return str(f'Com {idade} anos: Voto Negado.')
    elif idade >= 16 and idade <= 17:
        return str(f'Com {idade} anos: Voto Opcional.')
    elif idade >= 18 and idade <= 60:
        return str(f'Com {idade} anos: Voto Obrigatório.')
    elif idade > 65:
        return str(f'Com {idade} anos: Voto Opcional.')


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))

'''# Resolução do professor


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))'''