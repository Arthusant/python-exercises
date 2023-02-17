saque = int(input('Informe o valor a ser sacado: '))
print('-='*30)
print(f'PARA O SAQUE DE {saque} USAREMOS AS SEGUINTES CEDULAS...')
print('-='*30)
cedula_50 =cedula_20 =cedula_10 =cedula_1 = 0
while saque >= 50:
    saque -= 50
    cedula_50 += 1
while saque <50 and saque >=20:
    saque -= 20
    cedula_20 += 1
while saque <20 and saque >=10:
    saque -= 10
    cedula_10 += 1
while saque <10 and saque >=1:
    saque -= 1
    cedula_1 += 1
print(f'Cedulas de 50R$: {cedula_50}\n'
      f'Cedulas de 20R$: {cedula_20}\n'
      f'Cedulas de 10R$: {cedula_10}\n'
      f'Cedulas de 1R$:  {cedula_1}\n')
