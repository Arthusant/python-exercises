lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Quer continuar? '))
    if continuar in 'Nn':
        print('Encerrando programa!')
        break

lista.sort(key=int, reverse=True)

print(f'Foram digitados {len(lista)} valores!\n'
      f'Em ordem decrescente {lista}\n'
      f'O número 5 apareceu {lista.count(5)} vez(es) na lista')