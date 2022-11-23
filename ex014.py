# Escreva um programa que converta uma temperatura digitada em °C (Celsius) para °F (Fahrenheit).

t = float(input('Digite uma temperatura em °C: '))
f = t * 9 / 5 + 32
print('{}°C corresponde a {}°F'.format(t,f))
