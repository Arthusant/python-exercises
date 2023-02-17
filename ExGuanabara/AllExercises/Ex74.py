import random
numeros = (random.randint (0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
menor = numeros[1]
maior = numeros[1]
for i in range (len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print(f'Os números foram {numeros}\n'
      f'O maior número foi o {maior}\n'
      f'E o menor foi {menor}')
