lista = []
while True:
    valor = int(input('Digite o número: '))
    if valor in lista:
        print('Esse valor já foi adicionado anteriormente!')
    else:
        lista.append(valor)
        print('valor adicionado com sucesso')
    continuar = str(input('Quer continuar? (S \ N) '))
    if continuar in 'Nn':
        print('Programa encerrado!')
        break
lista.sort()
print(f'Os valores em ordem são {lista}')