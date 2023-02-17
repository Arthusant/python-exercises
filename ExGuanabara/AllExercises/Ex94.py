todos = list()
dados = dict()
idades = 0
todas_idades = []
mulheres = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: '))
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    todas_idades.append(dados['idade'])
    print(todas_idades)
    todos.append(dados.copy())
    idades += dados['idade']
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'nN':
        break
media_idd = idades/len(todos)
print(f'O grupo tem {len(todos)} pessoas')
print(f'A média de idade é {media_idd:.2} anos')
print(f'As mulheres cadastradas foram {mulheres}')
for i in range (len(todas_idades)):
    if todas_idades[i] > media_idd:
        print(f'{todos[i]["nome"]} tem a idade maior que a média, com {todas_idades[i]} anos')
