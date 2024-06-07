valor = int(input('Digite um numero inteiro: '))
valor_2 = int(input('Digite outro numero inteiro: '))

if valor > valor_2:
    print('O primeiro valor e maior.')
elif valor_2 > valor:
    print('O segundo valor é maior.')
else:
    print('Nenhum dos valores é maior. Pois eles são iguais.')
