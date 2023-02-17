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
