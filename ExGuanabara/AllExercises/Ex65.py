valor1 = int(input('Digite o número: '))
soma = 0
soma+=valor1
maior = 0
menor = valor1
continuar=str(input('Quer continuar? [SIM/NÃO]'))
while continuar in 'sS':
    valor1 = int(input('Digite o número: '))
    continuar=str(input('Quer continuar? [SIM/NÃO]'))
    soma += valor1
    if valor1 > maior:
        maior = valor1
    if valor1 < menor:
        menor=valor1
print(f'A soma dos valores é {soma}, o maior número foi {maior}, o menor foi {menor}')