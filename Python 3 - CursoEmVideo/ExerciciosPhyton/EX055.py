maior_peso = 0
menor_peso = 1000
nome_maior = ''
nome_menor = ''

for c in range(1, 5):
    
    nome = str(input('Qual o nome da {}° pessoa: '.format(c)).strip())
    peso = float (input('Qual o peso da {}° pessoa: '.format(c)))

    if peso > maior_peso:

        nome_maior = nome
        maior_peso = peso

    elif peso < menor_peso:

        nome_menor = nome
        menor_peso = peso

print('A pessoa com o maior peso foi {} com {}KG.'.format(nome_maior, maior_peso))
print('A pessoa com o menor peso foi {} com {}KG.'.format(nome_menor, menor_peso))