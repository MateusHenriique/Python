print('-='*20)
print('{:^40}'.format('JOGO PEDRA PAPEL E TESOURA'))
print('-='*20)

import random
from time import sleep

print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')
jogada_usuario = int(input('Qual será a sua escolha: '))
print('-='*20)
print('{:^40}'.format('Carregando...'))
print('-='*20)
sleep(5)
jogada_maquina = random.randint(1, 3)
if jogada_maquina == 1 and jogada_usuario == 2:
    print('Usuario: PAPEL!   x   Maquina: PEDRA!')
    print('Usuario VENCEU!')
elif jogada_maquina == 2 and jogada_usuario == 3:
    print('Usuario: TESOURA!   x   Maquina: PAPEL!')
    print('Usuario VENCEU!')
elif jogada_maquina == 3 and jogada_usuario == 1:
    print('Usuario: PEDRA!   x   Maquina: TESOURA!')
    print('Usuario VENCEU!')
elif jogada_usuario == 1 and jogada_maquina == 2:
    print('Usuario: PEDRA!   x   Maquina: PAPEL!')
    print('Usuario PERDEU!')
elif jogada_usuario == 2 and jogada_maquina == 3:
    print('Usuario: PAPEL!   x   Maquina: TESOURA!')
    print('Usuario PERDEU!')
elif jogada_usuario == 3 and jogada_maquina == 1:
    print('Usuario: TESOURA!   x   Maquina: PEDRA!')
    print('Usuario PERDEU!')


