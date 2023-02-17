primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro + (10-1) * razao
for i in range (primeiro, decimo+razao ,razao):
    print(f'{(i)}', end = '↣')
print('ACABOU')