print('-='*20)
print('ANALISADOR DE TRIANGULOS')                                      
print('-='*20)

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
print('-='*20)

#calculo retas
if (a + b > c) and (b + c > a) and (c + a > b):
    print('Essas retas podem formar um triangulo')
else:
    print('Essas retas não podem formar um triangulo.')
