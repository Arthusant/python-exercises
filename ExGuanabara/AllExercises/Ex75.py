c = (int(input('informe o primeiro valor: ')), int(input('informe o segundo valor: ')), int(input('informe o terceiro valor: ')),
         int(input('infome o quarto valor: ')))

par = []
for i in c:
    if i % 2 == 0:
        par.append(i)

print(f'Os números que você digitou foram:')
print(f'Dentre eles...')
print(f'O número 9 apareceu {c.count(9)} vezes!')
print(f'Os números pares foram {par}')

for i in c:
    if i == 3:
        indice_tupla = (c.index(3))
        print(f'O número 3 apareceu na {indice_tupla+1}ª posição!')
        break
