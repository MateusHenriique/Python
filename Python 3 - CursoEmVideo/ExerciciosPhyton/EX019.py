N1 = str(input('digite o 1° nome: '))
N2 = str(input('digite o 2° nome: '))
N3 = str(input('digite o 3° nome: '))
N4 = str(input('digite o 4° nome: '))
from random import choice
LISTA = [N1, N2, N3, N4]
print('o nome sorteado é: {}'.format(choice(LISTA)))

