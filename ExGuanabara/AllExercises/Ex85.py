lista_par = list()
lista_impar = list()
for i in range (0,6):
    numeros = int(input('Digite os números: '))
    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

print(f'DENTRE OS NÚMEROS DIGITADOS...\n'
      f'São impar {sorted(lista_impar)}\n'
      f'São par {sorted(lista_par)}')
