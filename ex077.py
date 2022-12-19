# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ()
teste = ''
for c in range(0, len(tupla)):
    vogais += ('a ' * tupla[c].count('a'),)
    teste += vogais[0]
    vogais += ('e ' * tupla[c].count('e'),)
    teste += vogais[1]
    vogais += ('i ' * tupla[c].count('i'),)
    teste += vogais[2]
    vogais += ('o ' * tupla[c].count('o'),)
    teste += vogais[3]
    vogais += ('u ' * tupla[c].count('u'),)
    teste += vogais[4]
    print(f'Na palavra {tupla[c]} temos {teste}')
    vogais = ()
    teste = ''

'''# Resolução do professor
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''
