PRECO = float(input('digite o preço do produto: R$'))
DESC = int(input('digite a porcentagem do desconto: %'))
NOVO_PRECO = (PRECO - ((PRECO / 100 )* DESC))
print('O preço do seu produto com {}% de desconto caiu de R${} para R${:.2f}'.format(DESC, PRECO, NOVO_PRECO))
