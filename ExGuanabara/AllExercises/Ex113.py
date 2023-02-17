def leiaint(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrupida pelo usúario!')
            return 0
        else:
            return valor

def leiafloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: por favor, Digite um número Real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrupida pelo usúariio!')
            return 0
        else:
            return valor


n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(n1, n2)
