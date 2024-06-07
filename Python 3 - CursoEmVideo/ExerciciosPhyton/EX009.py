n1 = int(input('Qual numero você deseja ver a tabuada: : '))
print('A tabuada de {} é: '.format(n1))
print('-=' * 10)
c = 1
while c <= 10:                                          
    print('{} x {:2} = {}'.format(n1, c, (n1 * c))) 
    c = (c + 1)  
print('-=' * 10)
