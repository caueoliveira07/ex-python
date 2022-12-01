# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade. Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 25 anos: SÊNIOR e Acima: MASTER.

from datetime import date
nascimento = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
idade = ano - nascimento
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria Mirim.')
elif idade <= 14:
    print('Você está na categoria Infantil.')
elif idade <= 19:
    print('Você está na categoria Junior.')
elif idade <= 25:
    print('Você está na categoria Sênior.')
elif idade > 25:
    print('Você está na categoria Master.')
