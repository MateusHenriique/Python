ano_nascimento = int(input('Em qual ano você nasceu: '))
genero = str(input('Qual é o seu gênero:')).strip().capitalize()

from datetime import datetime

now = datetime.now()
ano_atual = now.year
idade = ano_atual - ano_nascimento

if  genero == 'Masculino':
    if idade < 18:
        anos_para_alistamento = 18 - idade
        ano_do_alistamento = ano_atual + anos_para_alistamento
        
        if anos_para_alistamento == 1:
            print('Você tem {} ano, falta {} anos para o seu alistamento.'.format(idade, anos_para_alistamento))
        else:
            print('Você tem {} anos, falta {} anos para o seu alistamento.'.format(idade, anos_para_alistamento))
        
        print('Você tera que se alistar em {}'.format(ano_do_alistamento))
    elif idade == 18:
        print('Você ja tem {} anos, e tem que se alistar IMEDIATAMENTE!'.format(idade))
    else:
        anos_para_alistamento = idade - 18
        ano_do_alistamento = ano_atual - anos_para_alistamento
        
        if anos_para_alistamento == 1:
            print('Você ja tem {} anos, e deveria ter se alistado a {} ano.'.format(idade, anos_para_alistamento))
        else:
            print('Você ja tem {} anos, e deveria ter se alistado a {} anos.'.format(idade,anos_para_alistamento))
        
        print('Seu alistamento foi em {}'.format(ano_do_alistamento))
else:
    print('Você não tem obrigatoriedade para se alistar.')
