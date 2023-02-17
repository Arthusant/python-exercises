numero = int(input('Informe o número para verificar se o mesmo é primo: '))
if numero >= 1:
    for i in range (1 , numero):
        if numero % i != 0:
            print (f'O número {numero} é primo!')
        else:
            print (f'O número {numero} não é primo!')
            break
elif numero == 0:
    print ('O número é zero!')
else:
    print ('O número é negativo!')