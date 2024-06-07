print('-='*40)
print('SIMULAÇÃO FINANCIAMENTO')
print('-='*40)

valor_casa = float(input('qual o valor da casa que voce deseja financiar: '))
valor_salario = float(input('qual o valor do seu asalario atual: '))
parcelas = int(input('em quantos anos voce deseja financiar o imovel: '))
prestacao_mensal = valor_casa / (parcelas * 12)
print('o valor das prestacoes ficariam R${:.2f}'.format(prestacao_mensal))

if (valor_salario / 100 * 30 < prestacao_mensal):
    print('-='*40)
    print('FINANCIAMENTO NEGADO')
    print('sua renda nao e o suficiente para bater o valor minimo para financiar um imovel deste valor.')
    print('-='*40)
else:
    print('-='*40)
    print('FINANCIAMENTO APROVADO')
    print('Você atente os requisitos minimos para o financiamento caso aja interece em finalizar o financiamento, comparecer a uma agencia!')
    print('-='*40)