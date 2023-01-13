# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será quardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
gols = list()
total = int()
for p in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
print('-' * 40)
for i in gols:
    total += i
dicionário = {'nome': nome, 'gols': gols[:], 'total': total}
print(dicionário)
print('-' * 40)
for k, v in dicionário.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 40)
print(f'O jogador {nome} jogou {partidas} partidas.')
c = 1
for g in gols:
    print(f'Na partida {c}, fez {g} gols.')
    c += 1
print(f'Foi um total de {total} gols.')

'''# Resolução do professor
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gls na partida{c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
