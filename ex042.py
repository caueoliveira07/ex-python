# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado. Equilátero: todos os lados iguais, Isósceles: dois lados iguais e Escaleno: todos os lados diferentes.

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
ordem = [r1, r2, r3]
maior = max(ordem)
ordem.remove(maior)
a = ordem[0]
b = ordem[1]
if maior < a + b:
    print('É possível formar um triângulo.')
    if r1 == r2 and r2 == r3:
        # r1 == r2 == r3
        print('O triângulo será Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo será Isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        # r1 != r2 != r3 != r1
        print('O triângulo será Escaleno.')
else:
    print('Não é possível formar um triângulo.')
