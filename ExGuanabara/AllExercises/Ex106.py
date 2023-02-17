def ajuda(com):
    print('\033[41m~^\033[m'*14)
    print('\033[41mSistema de Ajuda PyHelp\033[m')
    print('\033[41m~^\033[m' * 14)
    help(com)


comando = ''
while True:
    comando = str(input('\033[44mFunção ou Biblioteca > \033[m'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
