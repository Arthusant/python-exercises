def voto():
    from datetime import date
    atual = date.today().year
    idd = atual-nasci
    if idd >= 18 and idd <=70: print('OBRIGATÓRIO')
    if idd >= 16 and idd <18: print('OPCIONAL')
    if idd >=0 and idd <16: print('NEGADO')
    if idd > 70: print('OPCIONAL')


nasci = int(input('Qual a data de nascimento? '))
voto()