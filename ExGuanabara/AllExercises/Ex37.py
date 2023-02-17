conversao = str(input('Informe a base decimal: '))
numero = int(input('Informe o numero que deseja converter:'))
guarda = []
if conversao == '1':
    while numero > 0:
        numero1 = numero % 2
        guarda.append(numero1)
        numero //= 2
    print (guarda[::-1])

if conversao == '2':
    while numero > 0:
        numero1 = numero % 8
        guarda.append(numero1)
        numero //= 8
    print (guarda[::-1])

if conversao == '3':
    print (hex(numero))

