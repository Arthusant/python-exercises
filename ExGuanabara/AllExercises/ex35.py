lista = []
for i in range (0,3):
    retas = int (input('Informe o valor de uma reta: '))
    lista.append (retas)
if ((lista[0]) + (lista[1])) > (lista[2]) and ((lista[1]) + (lista[2])) > (lista[0]) and ((lista[2]) + (lista[1])) > (lista[0]):
    print ('esses valores podem retornar um triangulo')
else:
    print ('Com esses valores não é possivel formar um triangulo!')
