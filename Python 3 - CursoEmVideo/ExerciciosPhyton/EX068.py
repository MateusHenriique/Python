import random
from time import sleep
 
print('-='*20)
print('{:^40}'.format('J O K E N P Ô'))
print('-='*20)
seguidas = 0

while True:

    PoI_jogador = str(input('Par ou Impar? ')).strip().lower()

    if PoI_jogador == 'par':

        PoI_maquina = 'impar'

    else:

        PoI_maquina = 'par'

    jogador = int(input('Digite um numero entro 1 e 10: '))
    maquina = random.randint(1, 10)
    PoI = jogador + maquina
    print('-='*20)
    print(f'Jogador: {PoI_jogador} {jogador}')
    print(f'Maquina: {PoI_maquina} {maquina}')
    print('-='*20)

    if PoI_jogador == 'par':

        if PoI % 2 == 0:

            print(f'{jogador} + {maquina} é {PoI}, que é Par Jogador Venceu!!')
            print('-='*20)
            print('Vamos jogar Novamente...')
            print('-='*20)
            seguidas += 1

        else:

            print(f'{jogador} + {maquina} é {PoI}, que é Impar Maquina Venceu!!')
            print('-='*20)
            break

    if PoI_jogador == 'impar':

        if PoI % 2 == 1:

            print(f'{jogador} + {maquina} é {PoI}, que é Impar Jogador Venceu!!')
            print('-='*20)
            print('Vamos jogar Novamente...')
            print('-='*20)
            seguidas += 1

        else:

            print(f'{jogador} + {maquina} é {PoI}, que é Par Maquina Venceu!!')
            print('-='*20)
            break
    
print(f'Você ganhou {seguidas} rodadas seguidas!')