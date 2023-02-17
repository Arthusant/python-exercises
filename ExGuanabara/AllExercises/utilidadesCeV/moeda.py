def dobro(n, formato = False):
    n = n*2
    return n if formato is False else moeda(n)


def metade(n, formato = False):
    n = n/2
    return n if formato is False else moeda(n)


def aumentar(n, p = 0, formato = False):
    res = n + (n * p/100)
    return res if formato is False else moeda(res)


def diminuir(n, p = 0, formato = False):
    res = n - (n * p/100)
    return res if formato is False else moeda(res)


def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

def resumo(n, taxa = 0, taxar = 0):
    print('='*30)
    print('Resumo do Valor'.center(30))
    print('=' * 30)
    print()
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(n, True)}')
    print(f'{taxar}% de redução: \t{diminuir(n,  True)} ')
    print()
    print('=' * 30)