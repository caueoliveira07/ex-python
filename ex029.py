# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input('Velocidade: '))
if km > 80:
    km = km - 80
    multa = km * 7.00
    print('Você foi multado.')
    print('O valor da multa é R${:.2f}'.format(multa))
else:
    print('Você não foi multado.')
