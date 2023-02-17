import random

numero_random = random.randint(0,10)
numero = int(input('Tente adivinhar o número que a maquina está pensando: '))
while numero_random != numero:
    numero = int(input('Tente mais uma vez: '))
print('Finalmente você acertou!')