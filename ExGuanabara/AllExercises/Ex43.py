nome = str(input('Qual o nome da pessoa: '))
altura = float(input('Informe qual a altura: '))
if "," in altura:
    str(altura).replace(',''.')
peso = float(input('Informe qual o peso: '))
imc = altura / (peso**2)
if imc < 18.5:
    print(f'{nome} está abaixo do peso!')
if imc > 18.5 or imc < 25:
    print(f'{nome} está no peso ideal!')
if imc > 25 or imc < 30:
    print(f'{nome} está com sobrepeso!')
if imc > 30 or imc < 40:
    print(f'{nome} está com obesidade!')
if imc > 40:
    print(f'{nome} está com obesidade mórbida!')
