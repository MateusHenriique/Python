print('{:=^40}'.format(' LOJA DO MATEUS '))
preco = float(input('Digite o valor do produto: R$ '))
print('{:=^40}'.format(' FORMAS DE PAGAMENTO '))
print('[ 1 ] À vista')
print('[ 2 ] Cheque ')
print('[ 3 ]À vista no cartão ')
print('[ 4 ] Parcelado no cartão ')
pagamento = int(input('Qual forma de pagamento você deseja: '))

if pagamento == 4:
    parcela = int(input('Em quantas vezes você quer parcelar: x'))

print('=' * 40)

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
    print('Em {} parcelas de R$ {:.2f}'.format(parcela, (desconto / parcela)))

else:
    
    print('Forma de pagamento incorreta!')