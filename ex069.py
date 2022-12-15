# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.

c = anos = homens = mulheres =  0
while c == 0:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        anos += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    continuar = str(input('Quer continuar? ')).upper()
    if continuar == 'S':
        c == 0
    elif continuar == 'N':
        c = 1
print('Fim do programa.')
print(f'Total de pessoas com mais de 18 anos: {anos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

'''# Resolução do professor
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')'''
