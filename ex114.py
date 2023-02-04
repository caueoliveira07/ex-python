# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

# Resolução do professor
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
    # Esse site.read() é só para mostrar o conteúdo HTML do site em questão.
