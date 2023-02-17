dados = list()

while True:
    temp = list()
    nome = str(input('Qual o nome do aluno? '))
    temp.append(nome)
    for i in range(2):
        nota = int(input(f'Qual a {i+1}º nota: '))
        temp.append(nota)
    continuar = str(input('Quer continuar? Sim/Não '))
    dados.append(temp[:])
    temp.clear()
    if continuar in 'nN':
        break
for i in dados:
   media = (i[1]+i[2])/2
   print(f'O aluno {i[0]} ficou com as notas {i[1]} e {i[2]}, ficando com a média {media}')
acesso = str(input('Você quer acessar a nota de algum aluno? '))
if acesso in 'Ss':
    aluno = str(input('De qual aluno você quer acessar? '))
    for a in dados:
        if a[0] == aluno:
            print(f'Essas são as notas de {a[0]}: {a[1]} e {a[2]}')