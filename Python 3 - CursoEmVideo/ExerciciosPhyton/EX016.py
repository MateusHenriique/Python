NUM = float(input('digite um numero quebrado: '))
print('a proporçao inteira de {} é {:.0f}'.format(NUM, int(NUM)))

#porem podemos usar a biblioteca math para resorver o poblema tambem
import math
NUM2 = float(input('digite outro numero quebrado: '))
print('a parte inteira de {} é {}'.format(NUM2, math.trunc(NUM2)))   