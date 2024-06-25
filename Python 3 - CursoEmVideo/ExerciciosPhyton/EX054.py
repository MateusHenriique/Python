from datetime import date

ano_atual = date.today().year
maior_de_idade = 0
menor_de_idade = 0

for c in range(1, 8):

    nascimento = int(input('Em qual ano a {}° pessoa nasceu: '.format(c)))
    idade = ano_atual - nascimento
    
    if idade < 18:

        menor_de_idade = menor_de_idade + 1

    else:

        maior_de_idade = maior_de_idade + 1

print('Das 7 pessoas digitadas {} são maiores de idade e {} são menores de idade!'.format(maior_de_idade, menor_de_idade))