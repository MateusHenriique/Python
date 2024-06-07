cateto_oposto = float(input('Digite o comprimento do cateto_oposto oposto: '))
cateto_adjecente = float(input('Digite o comprimento do cateto_oposto adjecente: '))
hip = (((cateto_oposto **2) + (cateto_adjecente ** 2)) ** (1 / 2)) 
print('O comprimendo da hipotenusa é: {:.2f}'.format(hip))

# Pode ser usado a biblioteca math para facilitar também.

from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto_oposto oposto: '))
cateto_adjecente = float(input('Digite o comprimento do cateto_oposto adjecente: '))
hip = hypot( cateto_oposto, cateto_adjecente)
print('O comprimendo da hipotenusa é: {:.2f}'.format(hip))
