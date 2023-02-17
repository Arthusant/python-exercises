dados = {}
list_gols = []
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for i in range (partidas):
    gol = int(input(f'Quantos gols na {i+1}º partida? '))
    list_gols.append(gol)
dados['gol'] = list_gols
tot = sum(list_gols)
dados['total'] = tot
print(dados)
print('=-' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
cont = 1
for c in list_gols:
    print(f'Na {cont}º partida fez {c} gols!')
    cont+=1