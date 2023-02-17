soma_idd = 0
maior_idade = 0
nome_velho = ''
cont_mulher = 0
for i in range(1,5):
    print(f'{i}ª PESSOA: ')
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: '))
    soma_idd += idade
    if i == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

    if idade < 20 and sexo in 'Ff':
        cont_mulher += 1

media_idade = soma_idd/4
print(f'A média da idade é de {media_idade}')
print(f'O homem mais velho é o {nome_velho} e sua idade é {maior_idade}')
print(f'A quantidade de mulheres com menos de 20 anos é {cont_mulher}! ')