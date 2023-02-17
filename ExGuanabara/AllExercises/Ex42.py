lado1 = int(input('Informe o primeiro lado do triangulo: '))
lado2 = int(input('Informe o segundo lado do triangulo: '))
lado3 = int(input('Informe o terceiro lado do triangulo: '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 <lado1):
        print('Nao é um triangulo')

if lado1 == lado2 and lado1 == lado3:
    print ('Esse triangulo é equilatero!')

if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ('Esse é um triangulo isósceles!')

else:
    print ('Esse é um triangulo Escaleno!')