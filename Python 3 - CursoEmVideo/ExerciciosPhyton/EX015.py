dias_carro = int(input('quantos dias voç~e ficou com o carro: '))
km_percorrido = float(input('quantos km foram percorridos com o carro: '))
tt_apagar = ((60 * dias_carro ) + (0.15 * km_percorrido))
print('Considerando uma diaria de R$60.00 e uma taxa de R$0,15 por km percorridos o total a pagar pelo aluguel do carro é de R${}'.format(tt_apagar))
