boletim = {'situação' : 0}
boletim['aluno'] = str(input('Qual o nome do aluno? '))
boletim['media'] = float(input('Qual a média do aluno? '))
if boletim['media'] <=10 and boletim['media'] >= 7:
    boletim['situaçao'] = 'Aprovado'
if boletim['media'] <7 and boletim['media'] >=5:
    boletim['situaçao'] = 'Recuperação'
if boletim['media'] <5 and boletim['media'] >=0:
    boletim['situaçao'] = 'Reprovado'
print(f'O aluno {boletim["aluno"]} ficou com a média {boletim["media"]}, com isso ele ficou {boletim["situaçao"]}')

