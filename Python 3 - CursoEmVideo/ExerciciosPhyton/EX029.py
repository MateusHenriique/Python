velocidade = float(input('voce esta a quantos KM/h: '))

if velocidade > 80:
    print('voce esta acima do limite de velocidade que é 80KM/h')
    multa = (velocidade - 80) * 7
    print('voce tera de pagar uma multa de R${:.2f}'. format(multa))
else:
    print('voce esta dentro do limite de velocidade. Parabens!')