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
print('{:^40}'.format('JO'))
sleep(1)
print('{:^40}'.format('KEM')) 
sleep(1)
print('{:^40}'.format('PO!!'))
print('-='*20)
jogada_maquina = random.randint(1, 3)
if jogada_maquina == 1 and jogada_usuario == 2:
    print('Usuario: PAPEL!   x   Maquina: PEDRA!')
    print('Usuario VENCE!')
elif jogada_maquina == 2 and jogada_usuario == 3:
    print('Usuario: TESOURA!   x   Maquina: PAPEL!')
    print('Usuario VENCE!')
elif jogada_maquina == 3 and jogada_usuario == 1:
    print('Usuario: PEDRA!   x   Maquina: TESOURA!')
    print('Usuario VENCE!')
elif jogada_usuario == 1 and jogada_maquina == 2:
    print('Usuario: PEDRA!   x   Maquina: PAPEL!')
    print('Maquina VENCE!')
elif jogada_usuario == 2 and jogada_maquina == 3:
    print('Usuario: PAPEL!   x   Maquina: TESOURA!')
    print('Maquina VENCE!')
elif jogada_usuario == 3 and jogada_maquina == 1:
    print('Usuario: TESOURA!   x   Maquina: PEDRA!')
    print('Maquina VENCE!')