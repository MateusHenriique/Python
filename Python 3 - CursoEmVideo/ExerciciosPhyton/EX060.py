continuar = ' '

while continuar != 'N':

    fatorial = int(input('Qual número Você deseja ver o fatorial: '))
    resultado_fatorial = 0
    print('Calculando o fatorial de {}! = {}'.format(fatorial, fatorial), end='')

    for multi in range(fatorial - 1, 1, -1):
        
        print(' x {}'.format(multi), end='')
        fatorial *= multi


    print(' = {}'.format(fatorial))

    continuar = str(input('Deseja Ver o Fatorial de outro número? [S, N]')).strip().upper()
print('Programa finalizado')
