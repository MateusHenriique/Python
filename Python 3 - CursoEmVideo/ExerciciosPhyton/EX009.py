n1 = int(input('digite um numro para ver a tabuada: '))
print('a tabuada de {} é: '.format(n1))
print('-' * 15)
c = 1
while c <= 10:                                          
    print('{} x {:2} = {}'.format(n1, c, (n1 * c))) 
    c = (c + 1)  
print('-' * 15)
