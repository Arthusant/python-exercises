pt = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 0
termo = pt
while cont <= 10:
    print(f'{termo}↠ ',end='')
    termo = termo+razao
    cont+=1



