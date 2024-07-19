while True:

    num = int(input('Qual numero você deseja ver a tabuada [numero negativo para parar]: '))

    if num < 0:

        break
    
    print('-='*20)

    for cont in range (1,11):

        mult = num * cont
        print(f'{num:} x {cont:2} = {mult}')

    print('-='*20)

print('Programa finalizado...') 