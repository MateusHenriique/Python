soma_multiplos = 0
tot = 0

for c in range(1, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            tot = tot + 1
            soma_multiplos = soma_multiplos + c

print('Entre 1 e 500, foram analizados {} numeros impares que são multiplos de 3.'.format(tot))
print('A soma desses numeros é {}'.format(soma_multiplos))