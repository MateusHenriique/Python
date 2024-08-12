nome_produto = str(input('Qual o nome do produto: ')).strip().capitalize()
preço_produto = float(input('Qual o valor do produto: ')) 
print('-='*20)

menor_valor = preço_produto
nome_barato = nome_produto
tot_mil = 0
tot_compras = 0

while True:

    if preço_produto > 1000:
        tot_mil += 1

    if  preço_produto < menor_valor:
        nome_barato = nome_produto
        menor_valor = preço_produto
        
    tot_compras += preço_produto

    continua = str(input('Quer comtinuar sua compra? [S/N]')).strip().upper()
    print('-='*20)

    if continua == 'N':
        break
    
    nome_produto = str(input('Qual o nome do produto: ')).strip().capitalize()
    preço_produto = float(input('Qual o valor do produto: '))


print(f'O valor total das suas compras foi de: R${tot_compras:.2f}')
print(f'Foram registrados {tot_mil} produtos que custam mais de R$1000 reais')
print(f'O produto com menor preço comprado foi {nome_barato} que custa {menor_valor}')
print('-='*20)