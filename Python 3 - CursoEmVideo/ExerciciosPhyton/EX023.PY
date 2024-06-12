n1 = int(input('digite um numero: '))
print('o numero {} tem: '.format(n1))
print('milhar: {}'.format((n1 // 1000 % 10)))
print('centena: {}'.format((n1 // 100 % 10)))
print('dezena: {}'.format((n1 // 10 % 10)))
print('unidade: {}'.format((n1 // 1 % 10)))
#para oegar uma determinada parte da str usar str[] com a posiçao que deseja dentro do colchete