# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: use cores.

from time import sleep
print('~' * 31)
print(f'    SISTEMA DE AJUDA PyHELP')
print('~' * 31)
while True:
    resp = str(input('Função ou Biblioteca > '))
    sleep(0.5)
    if resp.upper() == 'FIM':
        break
    else:
        print('~' * 43)
        print(f"    Acessando o manual do comando '{resp}'")
        print('~' * 43)
        sleep(1)
        help(resp)
        sleep(0.5)

'''# Resolução do professor
from time import sleep
c = ('\033[m' ,         # 0 - sem cores  
     '\033[0;30;41m',   # 1 - vermelho  
     '\033[0;30;41m',   # 2 - verde  
     '\033[0;30;41m',   # 3 - amarelo  
     '\033[0;30;41m',   # 4 - azul  
     '\033[0;30;41m',    # 5 - roxo  
     '\033[7;30m'       # 6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)'''
