salario = float(input('qual é o salario do funcionario: R$'))

#calculo aumento
if salario <= 1250.00:

    salario = salario + ((salario / 100) * 15)
    print('com base no seu salario anterior voce teve um aumento de 15%')
    
else:

    salario = salario + ((salario / 100) * 10)
    print('com base no seu salario anterior voce teve um aumento de 10%')

print('o seu novo salario e de R${:.2f}'.format(salario))
