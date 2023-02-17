jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for i in range (jogador['partidas']):
        gol = int(input(f'Quantos gols na {i+1}º partida: '))
        gols.append(gol)
    jogador['gol_'] = gols
    gols.clear()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    continuar = str(input('Quer continuar: '))
    if continuar in 'Nn':
        break
for k, v in enumerate(jogadores):
    print(f'{k:>4}' , end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

