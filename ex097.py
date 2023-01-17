# Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    for i in txt:
        print('~', end='')
    print('~' * 4)
    print(f'  {txt}')
    for i in txt:
        print('~', end='')
    print('~' * 4)
    

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
escreva(str(input('Digite a mensagem: ')))

'''# Resolução do professor
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')'''
