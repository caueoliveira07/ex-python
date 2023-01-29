# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Era pra ser 'from ex107 import moeda'.
import moeda
preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13)}')

'''# Resolução do professor
# O professor usou 'from ex107 import moeda', mas aqui não funcionou.
import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')'''
