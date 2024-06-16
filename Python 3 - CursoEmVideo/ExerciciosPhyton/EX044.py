preco = float(input('Digite o valor do produto: R$ '))
print('Qual será a forma de pagamento: ')
print('À vista [1]')
print('Cheque [2]')
print('À vista no cartão [3]')
print('parcelado no cartão [4]')
pagamento = int(input())
if pagamento == 4:
    parcela = int(input('Em quantas vezes você quer parcelar: x'))

if pagamento == 1:
    print('Você pagou à vista e recebeu um desconto de 10%')
    desconto = preco - ((preco / 100) * 10)
    print('O produto foi de R${:.2f} para R${:.2f}'.format(preco, desconto))
elif pagamento == 2:
    print('Você pagou no Cheque e recebeu um desconto de 10%')
    desconto = preco - ((preco / 100) * 10)
    print('O produto foi de R${:.2f} para R${:.2f}'.format(preco, desconto))
elif pagamento == 3:
    print('Você pagou à vista no cartão e recebeu um desconto de 5%')
    desconto = preco - ((preco / 100) * 5)
    print('O produto foi de R${:.2f} para R${:.2f}'.format(preco, desconto))
elif parcela <= 2:
    print('Você pagou em {}x no cartão e não recebeu desconto.'.format(parcela))
    print('Você pagou R$ {:.2f}'.format(preco))
elif parcela >=3:
    print('Você pagou em {}x no cartão e teve um juros de 20%'.format(parcela))
    desconto = preco + ((preco / 100) * 20)
    print('O produto foi de R${:.2f} para R${:.2f}'.format(preco, desconto))
else:
    print('Forma de pagamento incorreta!')