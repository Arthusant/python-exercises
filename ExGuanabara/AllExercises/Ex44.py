valor = float(input('Informe o valor do produto: '))
pagamento = str(input('Informe qual será a forma de pagamento: '))

if pagamento == 'dinheiro' or pagamento == 'a vista':
    porcent = valor * 0.1
    valor -= porcent
    print (f'O valor do produto ficou {valor}!')

if pagamento == 'cartão':
    forma = str(input('Dividido ou a vista? '))
    if forma == 'a vista':
        porcent = valor * 0.05
        valor -= porcent
        print(f'O valor do produto ficou {valor}!')

    if forma == 'dividido':
        vezes = int(input('Em quantas vezes? '))
        if vezes == 2:
            print(f'O valor do produto ficou {valor}!')
        if vezes > 2:
            porcent = valor * 0.20
            valor += porcent
            print(f'O valor do produto ficou {valor}!')


