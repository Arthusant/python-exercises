lista = list()
maispes=list()
maislev=list()
pessoas = 0
while True:
    x=list()
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    x.append(nome)
    x.append(peso)
    lista.append(x[:])
    continuar = str(input('Você quer continuar? '))
    if continuar in 'Nn':
        print('...')
        break
for p in lista:
        pessoas+=1
        if p[1] >=100:
            maispes.append(p)
        if p[1] <= 70:
            maislev.append(p)

print(f'foram cadastradas {pessoas} pessoas\n'
      f'As pessoas mais pesadas foram {maispes}\n'
      f'As pessoas mais leves foram {maislev}')
