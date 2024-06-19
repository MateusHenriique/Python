print('Em um intervalo entre 1 e 50 estes são os numeros pares: ')
total_pares = 0

for c in range(2, 51, 2):
    print(c, end=' ')
    total_pares = total_pares + 1

print('\nE o total de numeros pares que apareceram foi: {}'.format(total_pares))
