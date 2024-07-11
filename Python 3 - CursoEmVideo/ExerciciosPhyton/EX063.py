n = int(input('Quantos elementos da sequência Fibonacci você quer ver: '))
termo_1 = 0
termo_2 = 1
termo_3 = 0
print('{} - {}'.format(termo_1, termo_2), end=' - ')
c = 2

while c < n:

    termo_3 = termo_1 + termo_2
    print(termo_3, end=' - ')
    termo_1 = termo_2
    termo_2 = termo_3
    c += 1

print('FIM...')