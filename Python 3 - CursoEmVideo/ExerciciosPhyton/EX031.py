viagem = float(input('quantos Kilometros tera a sua viagem: '))

if viagem < 200:
    custo_viagem = viagem * 0.50
else:
    custo_viagem = viagem * 0.45
    
print('o custo da sua viagem sera : R${}'.format(custo_viagem))