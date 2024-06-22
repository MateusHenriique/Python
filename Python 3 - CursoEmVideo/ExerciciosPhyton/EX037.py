inteiro = int(input('Digite um numero inteiro: '))
print('-='*20)
print('Conversor De Inteiro')
print('-='*20)
print('[ 1 ] Converter para BINARIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
converte = int(input('Sua opção: '))

if converte == 1:

    print('O numero {} convertido em binario fica: {}'.format(inteiro, bin(inteiro)[2:]))    

elif converte == 2:

    print('O numero {} convertodo em octal fica: {}'.format(inteiro, oct(inteiro)[2:]))

elif converte == 3:

    hexadecimal = hex(inteiro)

    print('O numero {} convertido em hexadecimal fica: {}'.format(inteiro, hex(inteiro)[2:]))

else:
    
    print('Opção invalida tente novamente.')
