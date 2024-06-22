from datetime import date

nascimento = int(input('Digite o ano de nascimento do atleta: ')) 
ano_atual = date.today().year 
idade = ano_atual - nascimento

if idade <= 9:

    print('O atleta tem {} anos e se enquadra na categoria MIRIM.'.format(idade))

elif 9 < idade <= 14:

    print('O atleta tem {} anos e se enquadra na categoria INFANTIL.'.format(idade))

elif 14 < idade <= 19:

    print('O atleta tem {} anos e se enquadra na categoria JÚNIOR'.format(idade))

elif 19 < idade <= 25:

    print('O atleta tem {} anos e se enquadra na categoria SÊNIOR.'.format(idade))
    
else:

    print('O atleta tem {} anos e se enquadra na categoria MASTER.'.format(idade))
