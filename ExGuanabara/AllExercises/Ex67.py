numero = int(input('Quer ver a tabuada de qual número: '))
cont = 1
while cont != 10:
    print(f'{numero}*{cont}={numero * cont}')
    cont+=1
    if cont == 10:
        cont = 0
        numero = int(input('Quer ver a tabuada de qual número: '))
        if numero < 0:
            print('Saindo...')
            break