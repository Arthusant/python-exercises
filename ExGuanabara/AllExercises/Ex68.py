import random
cont = 0
cont_v = 0
while cont == 0:
    jogada = str(input('Impar ou Par? '))
    numero = int(input('Qual número? '))
    jogada_pc = random.randint(0,10)
    resultado = jogada_pc + numero
    if jogada == 'par':
        if resultado %2 == 0:
            print('Você venceu!')
            cont_v += 1
        else:
            print(f'PERDEU KKK, Você conseguiu vencer {cont_v} vezes! ')
            break
    elif jogada == 'impar':
        if resultado %2 == 1:
            print('Você venceu')
            cont_v +=1
        else:
            print(f'PERDEU KKK, Você conseguiu vencer {cont_v} vez(es)! ')
            break