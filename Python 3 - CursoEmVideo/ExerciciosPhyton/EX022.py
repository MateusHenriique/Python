NOME = str(input('digite o seu nome completo: ')).strip()
print('analisando o seu nome...')
print('O seu nome em maiusculo é: {}'.format(NOME.upper()))
print('O seu nome em minusculos é: {}'.format(NOME.lower()))
NOME2 = NOME.split()
print('No total seu nome tem {} letras'.format(len(''.join(NOME2))))
print('Seu primeiro nome é {} e tem {} letras'.format(NOME2[0], len(NOME2[0])))