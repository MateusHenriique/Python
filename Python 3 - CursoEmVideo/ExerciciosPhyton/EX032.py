from datetime import date

bissexto = int(input('que ano deseja analisar? 0 para o ano atual: '))

if bissexto == 0:

    bissexto = date.today().year 

if bissexto % 4 == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:
   
    print('o ano de {} ano e bissexto'.format(bissexto))

else:

    print('o ano de {} ano nao é bissexto'.format(bissexto))