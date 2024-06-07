DIAS_COM_CARRO = int(input('quantos dias voç~e ficou com o carro: '))
KM_PERCORRIDOS = float(input('quantos km foram percorridos com o carro: '))
TT_APAGAR = ((60 * DIAS_COM_CARRO ) + (0.15 * KM_PERCORRIDOS))
print('Considerando uma diaria de R$60.00 e uma taxa de R$0,15 por km percorridos o total a pagar pelo aluguel do carro é de R${}'.format(TT_APAGAR))
