num = float(input('digite um numero quebrado: '))
print('a proporçao inteira de {} é {:.0f}'.format(num, int(num)))

#porem podemos usar a biblioteca math para resorver o poblema tambem
import math
num2 = float(input('digite outro numero quebrado: '))
print('a parte inteira de {} é {}'.format(num2, math.trunc(num2)))   