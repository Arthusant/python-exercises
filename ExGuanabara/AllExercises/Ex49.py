numero=int(input('Informe o número que você quer a tabuada: '))
cont=0
print (f'A tabuada do número {numero} é:')
for i in range (0,9):
    cont+=1
    print(f'{numero}*{cont}={numero*cont}')