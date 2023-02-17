distancia = float(input('Qual a distância da viagem em KM: '))
if distancia < 200 and distancia >0:
    print(f'O valor da viagem de {distancia}KM, custará {distancia*0.50}R$')
elif distancia >200:
    print(f'O valor da viagem de {distancia}KM, custará {distancia*0.45}R$ ')