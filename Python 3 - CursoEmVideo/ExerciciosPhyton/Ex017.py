CATETO = float(input('digite o comprimento do cateto oposto: '))
CATETO_ADJECENTE = float(input('digite o comprimento do cateto adjecente: '))
HIP = (((CATETO **2) + (CATETO_ADJECENTE ** 2)) ** (1/2)) 
print('o comprimendo da hipotenusa é: {:.2f}'.format(HIP))

# pode ser usado a biblioteca math para facilitar tambem

from math import hypot
CATETO = float(input('digite o comprimento do cateto oposto: '))
CATETO_ADJECENTE = float(input('digite o comprimento do cateto adjecente: '))
HIP = hypot( CATETO, CATETO_ADJECENTE)
print('o comprimendo da hipotenusa é: {:.2f}'.format(HIP))
