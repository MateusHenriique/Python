sexo = str(input('Qual é o seu genero [M / F] : ')).strip().upper()

while sexo not in 'MmFf':
    
    sexo = str(input('Dado invalido, Por Favor, informe seu sexo: ')).strip().upper()

print('Sexo {} Registrado com sucesso'.format(sexo))
