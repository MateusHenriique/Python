print('-='*20)
print('{:^40}'.format('CADASTRO PESSOAS'))
print('-='*20)
mais_18 = tot_homens = 0

while True:

    str_idade = str(input('Digite a idade da pessoa: '))

    while True:

        if str_idade.isdigit() == True:

            idade = int(str_idade)

            while idade <= 0 or idade > 100:

                print('-='*20)
                print('idade invalida tente novamente...')
                idade = int(input('Digite a idade da pessoa: '))
            
            break

        else:
            
            print('-='*20)
            print('idade invalida tente novamente...')
            str_idade = (input('Digite a idade da pessoa: '))
        
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

    while sexo != 'M' and sexo != 'F' and sexo != 'MASCULINO' and sexo != 'FEMININO':

        print('-='*20)
        print('Sexo incorreto tente novamente....')
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

    print('-='*20)
    continua = str(input('Deseja Cadastrar outra pessoa [S/N]: ')).strip().upper()

    while continua != 'S' and continua != 'N':

        print('-='*20)
        print('Resposta incorreta tente novamente...')
        continua = str(input('Deseja Cadastrar outra pessoa [S/N]: ')).strip().upper()

    if idade > 18:

        mais_18 += 1

    if sexo == 'M' or sexo == 'MASCULINO':

        tot_homens += 1

    if continua == 'N':

        break

print('-='*20)
print(f'O total de pessoas com mais de 18 anos cadastradas foram: {mais_18}')
print(f'O total de homens cadastrados foram: {tot_homens}')