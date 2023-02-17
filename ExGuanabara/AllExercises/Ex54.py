cont = 0
for i in range (0,7):
    ano = int(input('Informe o ano de nascimento: '))
    if ano <= 2004:
        cont +=1
print (f'A quantidade de pessoas que atingiram a maioridade foram {cont}')