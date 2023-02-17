lista = []
cont = 0
print ('-'*35)
for i in range (0,2):
    numero = int(input(f'Digite o {cont + 1}º número inteiro: '))
    lista.append(numero)

if lista[0] == lista[1]:
    print('Os valores são iguais')
else:
    print(f'o maior valor digitado foi o {max(lista)} e o menor número foi {min(lista)}')
