# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase)
print('A frase invertida ficará assim:\n{}'.format(frase[::-1].replace(' ', '')))
if frase.replace(' ', '') == frase[::-1].replace(' ', ''):
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
    