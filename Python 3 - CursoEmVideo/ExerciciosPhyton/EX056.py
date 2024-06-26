soma_idade = 0
maior_idade = 0
Menor_que_20 = 0
media_idade = 0
maior_nome = ''

for c in range(1,5):

    print('{:=^30}'.format(' {}° PESSOA '.format(c)))
    nome = str(input('Digite o nome: '.format(c)))
    idade = int(input('Digite a idade: '.format(c)))
    sexo = str(input('Digite o sexo: [M / F]'.format(c)).upper())

 
    soma_idade = soma_idade + idade

    if sexo == 'M' and idade > maior_idade:

        maior_nome = nome
        maior_idade = idade

    if sexo == 'F' and idade < 20:

        Menor_que_20 = Menor_que_20 + 1

media_idade = soma_idade / 2
print('A media das idades digitadas foi de: {}'.format(media_idade))
print('Dos homens o mais velho é {} com {} anos.'.format(maior_nome, maior_idade))
print('No total foram digitadas {} mulheres com menos de 20 anos.'.format(Menor_que_20))