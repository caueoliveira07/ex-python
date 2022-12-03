# Refaça o DESAFIO 009, mostrando  a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver a tabuada: '))
for m in range(0, 11):
    print('{} x {} = {}'.format(n, m, n * m))
