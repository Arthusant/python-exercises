lista = []
for i in range(0,4):
    valor = int(input('Digite os números: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos +=1
print(f'Os valores digitados em ordem foram: {lista}')
