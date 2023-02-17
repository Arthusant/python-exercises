lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    continuar = str(input('Quer continuar? Sim/Não '))
    if continuar in 'Nn':
        print('Os resultados foram: ')
        break
print(f'Todos os números digitados foram {lista}\n'
      f'Dentre eles...\n'
      f'São PAR: {lista_par}\n'
      f'São IMPAR: {lista_impar}')