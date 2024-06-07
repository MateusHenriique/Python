N1 = int(input('digite um numero: '))
print('o numero {} tem: '.format(N1))
print('milhar: {}'.format((N1 // 1000 % 10)))
print('centena: {}'.format((N1 // 100 % 10)))
print('dezena: {}'.format((N1 // 10 % 10)))
print('unidade: {}'.format((N1 // 1 % 10)))
#para oegar uma determinada parte da str usar str[] com a posiçao que deseja dentro do colchete