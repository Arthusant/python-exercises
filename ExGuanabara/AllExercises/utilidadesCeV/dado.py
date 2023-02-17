def leiadinheiro(p):
    numero = (input(p)).replace(',' , '.')
    valor = False
    while valor is False:
        if numero.isalpha() or numero.strip() == '':
            numero = (input(f'{numero} é um preço inválido!\n'
                            f'{p}'))
        else:
            valor = True
            return float(numero)






