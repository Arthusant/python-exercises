import random
numeros = []

def sortear():
    print('sorteando 5 valores')
    for i in range(0,5):
        sorteio = random.randint(0, 10)
        numeros.append(sorteio)
    print(f'Os 5 valores sorteados foram: {numeros}')
def somaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'A soma entre todos os valores pares da lista {numeros} é {soma}')

sortear()
somaPar()



