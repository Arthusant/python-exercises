ano = int(input('Informe a data do seu nascimento: '))
idade =  2022 - ano
if idade <=9 and idade >0:
    print (f'Você tem {idade} anos, então faz parte da categoria mirim!')
if idade >9 and idade <=14:
    print(f'Você tem {idade} anos, então faz parte da categoria infantil!')
if idade >14 and idade <= 19:
    print(f'Você tem {idade} anos, então faz parte da categoria Junior!')
if idade >19 and idade <20:
    print(f'Você tem {idade} anos, então faz parte da categoria sênior!')
if idade >20:
    print(f'Você tem {idade} anos, então faz parte da categoria master!')
