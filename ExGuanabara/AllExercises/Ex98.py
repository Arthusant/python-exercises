import time


def contador(i, f, m):
    print(f'contagem de {i} até {f}, de {m} em {m}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end = ' ')
            time.sleep(0.5)
            cont+=m
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            time.sleep(0.5)
            cont-=m
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
contador((int(input('Inicio: '))), (int(input('Fim: '))), (int(input('Pulando: '))))