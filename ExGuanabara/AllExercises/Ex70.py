total = 0
mais_1000 = 0
mais_barato = ''
valor_barato = 0
cont = 1
while True:
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? '))
    valor_barato = valor
    total += valor
    cont+=1
    if valor >= 1000:
        mais_1000 += 1

    if valor < valor_barato:
        valor_barato = valor
        mais_barato = nome

    continuar = str(input('Quer continuar? (S/N) '))
    if continuar in 'Nn':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        print (f'O total da compra foi: {total} \n'
               f'A quantidade de produtos que custam mais de 1000 R$ foram {mais_1000}\n'
               f'O nome do produto mais barato é {mais_barato} e custa {valor_barato}')
        break