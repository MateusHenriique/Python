nome = str(input('digite o seu nome completo: ')).strip()
print('analisando o seu nome...')
print('O seu nome em maiusculo é: {}'.format(nome.upper()))
print('O seu nome em minusculos é: {}'.format(nome.lower()))
nome2 = nome.split()
print('No total seu nome tem {} letras'.format(len(''.join(nome2))))
print('Seu primeiro nome é {} e tem {} letras'.format(nome2[0], len(nome2[0])))

