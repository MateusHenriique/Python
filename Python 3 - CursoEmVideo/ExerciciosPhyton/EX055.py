maior_peso = 0
menor_peso = 0
nome_maior = ''
nome_menor = ''

for c in range(1, 6):

    nome = str(input('Qual o nome da {}° pessoa: '.format(c)).strip())
    peso = float (input('Qual o peso da {}° pessoa: '.format(c)))

    if c == 1:

        menor_peso = peso
        maior_peso = peso
        nome_menor = nome
        nome_maior = nome

    else:

        if peso > maior_peso:

            nome_maior = nome
            maior_peso = peso

        elif peso < menor_peso:

            nome_menor = nome
            menor_peso = peso

print('A pessoa com o maior peso foi {} com {:.2f}KG.'.format(nome_maior, maior_peso))
print('A pessoa com o menor peso foi {} com {:.2f}KG.'.format(nome_menor, menor_peso))
