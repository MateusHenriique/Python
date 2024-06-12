preco = float(input('digite o preço do produto: R$'))
desc = int(input('digite a porcentagem do desconto: %'))
novo_preco = (preco - ((preco / 100 )* desc))
print('O preço do seu produto com {}% de desconto caiu de R${} para R${:.2f}'.format(desc, preco, novo_preco))
