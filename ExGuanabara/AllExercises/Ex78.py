cont = 0
lista =[]
maior = 0
pos_maior = 0
pos_menor = 0
valores = int(input(f'informe o valor da posição {cont}º: '))
lista.append(valores)
menor = valores
for i in range (0, 4):
    cont+=1
    valores = int(input(f'informe o valor da posição {cont}º: '))
    lista.append(valores)
    if valores < menor:
        menor = menor
        pos_menor = cont
    if valores > maior:
        maior = valores
        pos_maior = cont

print(f'O maior valor digitado foi {maior} e estava na posição {pos_maior}\n'
      f'O menor valor digitado foi {menor} e estava na posição {pos_menor}')