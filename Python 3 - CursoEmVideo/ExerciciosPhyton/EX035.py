print('-='*20)
print('ANALISADOR DE TRIANGULOS')
print('-='*20)

a = float(input('digite o comprimento da primeira reta: '))
b = float(input('digite o comprimento da segunda reta: '))
c = float(input('digite o comprimento da terceira reta: '))
print('-='*20)

#calculo retas
if (a + b > c) and (b + c > a) and (c + a > b):
    print('essas retas podem formar um triangulo')
else:
    print('essas retas nao podem formar um triangulo')
