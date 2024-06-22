n1 = int(input('Qual numero você deseja ver a tabuada: : '))
print('-=' * 10)
print('A tabuada de {} é: '.format(n1))
print('-=' * 10)
c = 1

for c in range(1, 11):                                    
    print('{} x {:2} = {}'.format(n1, c, (n1 * c)))  
print('-=' * 10)
