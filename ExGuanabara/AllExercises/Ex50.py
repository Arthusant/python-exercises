lista = []
for i in range (6):
    numero = int(input('Informe os número: '))
    if numero % 2 == 0:
        lista.append(numero)
print(sum(lista))