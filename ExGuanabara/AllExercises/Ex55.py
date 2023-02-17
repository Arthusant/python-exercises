peso2 = float(input('Informe os pesos: '))
menor_peso = peso2
maior_peso = peso2
for i in range (0,5):
    peso = float(input('Informe os pesos: '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(menor_peso,maior_peso)
