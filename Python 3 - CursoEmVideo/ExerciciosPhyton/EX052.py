if_primo = int(input('Digite um numero inteiro: '))
divisivel = 0

if if_primo % 1 == 0 and if_primo % if_primo == 0:

    for c in range(1, if_primo + 1):
        
        if if_primo % c == 0:

            print('\033[1;31m {}'.format(c), end='')
            divisivel = divisivel + 1

        else:

            print('\033[1;33m {}'.format(c), end='')

    if divisivel < 2: 
        
        print('\n\033[0;0mO numero {} foi divisivel {} vezes.'.format(if_primo, divisivel))
        print('\033[0;0m{} é um número primo.'.format(if_primo))

    else:

        print('\n\033[0;0mO numero {} foi divisivel {} vezes.'.format(if_primo, divisivel))
        print('\033[0;0m{} não é um número primo.'.format(if_primo))
