qnt = int(input('informe quantos termos você quer mostrar: '))
qnt-=2
t1 = 0
t2 = 1
print(f'{t1} ⇝ {t2}',end='')
while qnt != 0:
    t3 = t1 + t2
    print(f' ⇝ {t3}',end='')
    t1=t2
    t2=t3
    qnt -= 1
print(' ⇝ Fim')
