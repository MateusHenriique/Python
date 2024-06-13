n1 = str(input('digite o 1° nome: '))
n2 = str(input('digite o 2° nome: '))
n3 = str(input('digite o 3° nome: '))
n4 = str(input('digite o 4° nome: '))

from random import shuffle

lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem para a apresentação do trabalho é: {}'.format(lista))