frase = (str(input('Informe a frase: ')))
x = frase.replace('',' ')
sep = x.split()
invert = list(reversed(sep))
if sep == invert:
    print(f'é polindro!')
else:
    print('Não é polindro!')