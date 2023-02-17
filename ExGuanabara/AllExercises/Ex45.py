import random

print ('Vamos começãr o jogo :) ')
print(26*'_')
print('Pedra = 1\nPapel = 2\nTesoura = 3')
print(26*'_')
jogador = int(input('Qual sua jogada: '))
maquina = random.randint(1,3)
print (f'Você escolheu {jogador} e eu escolhi {maquina}, então...')
if jogador == maquina:
    print (f'Ops, Parece que deu empate, eu escolhi {maquina}')
if jogador == 2 and maquina == 1:
    print ('Você venceu!')
if jogador == 1 and maquina == 3:
    print('Você venceu!')
if jogador == 3 and maquina == 2:
    print('Você venceu!')
if jogador == 1 and maquina == 2:
    print ('kk vc perdeu')
if jogador == 3 and maquina == 1:
    print('kk vc perdeu')
if jogador == 2 and maquina == 3:
    print('kk vc perdeu')