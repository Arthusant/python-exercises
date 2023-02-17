dados = dict()
dados['nome'] = str(input('Nome? '))
nasci = int(input('Ano de Nascimento: '))
dados['idade'] = 2023 - nasci
cdt = int(input('Carteira de Trabalho: '))
if cdt <= 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
    dados['ctps'] = cdt
else:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    colab = 2023 - dados['contratação']
    dados['colaboração'] = (35 - colab) + dados['idade']
    print('=-' * 40)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')


