nota1=float(input('Informe a primeira nota do aluno: '))
nota2=float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media <=5.0:
    print (f'O aluno ficou com a média {media}, então foi reprovado!!')
if media >5.0 and media < 6.9:
    print (f'o aluno ficou com a media {media}, então está na recuperação!!')
if media >=7.0 and media <=10:
    print (f'O aluno ficou com a média {media}, então está aprovado!!')