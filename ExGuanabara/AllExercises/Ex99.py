def maior(num):
    print(max(num))


lista = []
while True:
    num = int(input('Digite o número: '))
    lista.append(num)
    continuar = str(input('Quer continuar? '))
    if continuar in 'nN':
        break
maior(lista)