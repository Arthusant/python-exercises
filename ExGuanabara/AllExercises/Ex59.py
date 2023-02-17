p_numero = int(input('Informe o primeiro número: '))
s_numero = int(input('Informe o segundo número: '))
opera = int(input('[1] soma\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'
                  'Qual operação você quer realizar? '))
while opera != 5:
    if opera == 1:
        print(f'A soma dos dois números é {p_numero + s_numero}!')

    if opera == 2:
        print(f'O resultado da multiplicação entre esses dois números é {p_numero * s_numero}')

    if opera == 3:
        if p_numero>s_numero:
            print('O primeiro número é o maior!')

        elif s_numero>p_numero:
            print('O segundo número é o maior!')

        else:
            print('Os números são iguais!')

    if opera == 4:
        p_numero = int(input('Informe o primeiro número: '))
        s_numero = int(input('Informe o segundo número: '))

    opera = int(input('[1] soma\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'
                      'Qual operação você quer realizar? '))

print('PROGRAMA FECHADO!')