numero1 = int (input('informe o primeiro numero: '))
numero2 = int (input('informe o segundo numero: '))
numero3 = int (input('informe o terceiro numero: '))
if numero1 < numero2 and numero1 < numero3:
    print ('O primeiro numero informado é o menor')
elif numero2 < numero1 and numero2 < numero3:
    print('O segundo numero informado é o menor')
elif numero3 < numero1 and numero3 < numero2:
    print('O terceiro numero informado é o menor')