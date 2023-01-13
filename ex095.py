# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista = list()
cod = int()
while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = list()
    total = int()
    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    for i in gols:
        total += i
    dicionário = {'cod': cod, 'nome': nome, 'gols': gols, 'total': total}
    lista.append(dicionário.copy())
    cod += 1
    resp = str(input('Quer continuar? [S/N] '))[0]
    if resp in 'Nn':
        break
print('-' * 50)
print(f'{"cod":<4}{"nome":<16}{"gols":<16}{"total"}')
print('-' * 50)
cod = int()
for i in lista:
    print(f'{cod:<4}{i["nome"]:<16}{i["gols" ]}{"":<16}{i["total"]}')
    cod += 1
print('-' * 50)
while True:
    resp = int(input('Mostrar dados de qual jogador? '))
    if resp == 999:
        break
    cod = int()
    for i in lista:
        cod += 1
    if resp > cod - 1:
        print(f'Erro! não existe jogador com código {resp}! Tente novamente.')
    p = 1
    c = 0
    for i in lista:
        if i['cod'] == resp:
            print(f'Levantamento do jogador {i["nome"]}:')
            for i in lista[resp]['gols']:
                print(f'No jogo {p} fez {lista[resp]["gols"][c]} gols.')
                p += 1
                c += 1

'''# Resolução do professor
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print(' << VOLTE SEMPRE >>')'''
