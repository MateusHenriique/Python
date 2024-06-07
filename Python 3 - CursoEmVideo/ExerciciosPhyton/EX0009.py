N1 = int(input('digite um numro para ver a tabuada: '))
print('a tabuada de {} é: '.format(N1))
print('-' * 15)
C = 1 # variavel para contador
while C <= 10: # while 'funçao enquanto' para fazer repetições necessario ' : ' para funcionar 
    # {:2} as as chaves servem para determinar a quantidade de espaços que vao ser usados, {:2f}a com o f w para numeros depois da virgula                                               
    print('{} x {:2} = {}'.format(N1, C, (N1 * C))) 
    C = (C + 1)  
print('-' * 15)
