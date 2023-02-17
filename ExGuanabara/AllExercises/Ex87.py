matriz = [[],[],[]]
linha = 0
par = []
coluna_3 = []
linha_1 = []
while True:
    coluna = 0
    while coluna !=3:
        valor = int(input(f'Linha {linha} Coluna {coluna}: '))
        if valor % 2 == 0:
            par.append(valor)
        matriz[linha].append(valor)
        if coluna == 2:
            coluna_3.append(valor)
        if linha == 1:
            linha_1.append(valor)
        coluna += 1

    linha+=1
    if linha == 3:
        break
maior = max(linha_1)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma de todos os valores pares digitados é {sum(par)}\n'
      f'A soma dos valores da terceira coluna é {sum(coluna_3)}\n'
      f'O maior valor da segunda linha foi {maior}')