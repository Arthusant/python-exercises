itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
x = 'LISTAGEM DE PREÇO'
print('-='*30)
print(f'LISTAGEM DE PREÇO'.center(60))
print('-='*30)
for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<30}', end = '')
    else:
        print(f'{itens[i]:>7}')

