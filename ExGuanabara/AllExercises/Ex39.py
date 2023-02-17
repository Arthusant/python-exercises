nasci = int(input('Informe o ano que vc nasceu: '))
idade = 2022 - nasci
if idade == 18:
    print ('Está na hora de se alistar!')
if idade < 18:
    print (f'Ainda não esta na hora de se alistar, que tal daqui {18-idade}!')
if idade > 18:
    print (f'Já passou da hora de se alistar, devia ter se alistado há {idade-18}!')
