# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza primeiro = Ana último = Souza

n = str(input('Nome completo: '))
nome = n.split()
print(nome[0], nome[-1])
# print('Seu último nome é {}'.format(nome[len(nome)-1]))
