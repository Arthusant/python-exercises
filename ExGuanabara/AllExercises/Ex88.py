import random
import time

cont = 0
jogos = list()
temp = list()
quantos = int(input('Quantos jogos você irá fazer? '))
for i in range (quantos):
    for c in range(6):
        ale = random.randint(1, 60)
        temp.append(ale)
    jogos.append(temp[:])
    temp.clear()
time.sleep(1)
print('-=' * 3, f'SORTEANDO {quantos} JOGOS', '-=' * 3)
time.sleep(2)
for c in jogos:
    cont += 1
    print(f'{cont}º jogo {c}')
    time.sleep(2)
