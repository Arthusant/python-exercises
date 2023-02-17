numero = int(input('Digite os números: '))
soma = 0
soma += numero
cont = 0
while numero != 999:
    numero = int(input('Digite os números: '))
    soma += numero
    cont+=1

print(f'A quantidade de números digitados foram {cont} e a soma foi {soma-999}')