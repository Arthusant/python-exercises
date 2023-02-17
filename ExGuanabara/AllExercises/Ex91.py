import random
import time
import operator
jogo = {'jogador 1': random.randint(1,6),
        'jogador 2': random.randint(1, 6),
        'jogador 3': random.randint(1, 6),
        'jogador 4': random.randint(1, 6)
        }
ranking = dict()
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado!')
    time.sleep(1)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}. ')
    time.sleep(1)