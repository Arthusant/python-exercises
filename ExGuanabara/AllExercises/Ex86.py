matriz = [[],[],[]]
linha = 0
while True:
    coluna = 0
    while coluna !=3:
        valor = int(input(f'Linha {linha} Coluna {coluna}: '))
        matriz[linha].append(valor)
        coluna += 1
    linha+=1
    if linha == 3:
        break
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

