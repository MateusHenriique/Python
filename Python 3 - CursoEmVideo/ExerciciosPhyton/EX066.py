tot_valor = soma = valor = 0

while True:

    valor = int(input('Digite um numero inteiro [999 para parar]: '))

    if valor == 999:

        break

    tot_valor += 1
    soma += valor

print(f'O total de valores digitados foi {tot_valor} e a soma dos valores é {soma}. ')
