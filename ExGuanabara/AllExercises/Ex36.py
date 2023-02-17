valor_cs = float (input ('Informe o valor da casa: '))
salario = float(input('Informe o salario do comprador: '))
anos = int(input('Em quantos anos vc planeja terminar de pagar? '))
anos *= 12
prestacao = valor_cs / anos
salario_30 = salario * 0.3
if salario_30 < prestacao:
    print ('Infelizmente seu imprestimo foi negado')
else:
    print ('Parabéns, seu empréstimo foi aprovado!')