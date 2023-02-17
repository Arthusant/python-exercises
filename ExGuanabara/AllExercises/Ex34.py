salario = float(input('Informe o valor do salario: '))
if salario > 1250.00:
    adicional = salario * 0.1
    salario += adicional
else:
    adicional2 = salario * 0.15
    salario += adicional2

print (f'O salario desse funcionario ficará de {salario}')
