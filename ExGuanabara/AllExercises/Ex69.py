cont = 0
mais_18 = 0
hom = 0
fem_20 = 0
while cont  == 0:
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? (F/M) '))
    if idade >= 18:
        mais_18 += 1
    if sexo in 'Mm':
        hom += 1
    if sexo in 'Ff' and idade >= 20:
        fem_20 += 1
    pros = str(input('Quer continuar? (Sim/Não)'))
    if pros in 'nN':
        print(f'A quantidade de pessoas com mais de 18 anos é de {mais_18}\n'
              f'A quantidade de homens cadastrados é de {hom}\n'
              f'A quantidade de mulheres com mais de 20 é de {fem_20}\n')
        break

