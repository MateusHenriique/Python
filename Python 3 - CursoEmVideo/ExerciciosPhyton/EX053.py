frase = str(input('Digite uma frase: ')).strip()
frase_2 = frase.split()
frase_3 = ''.join(frase)
palindromo = frase_3[::-1]
print('O inverso de {} é {}'.format(frase, frase[::-1]))

if frase == palindromo:

    print('A frase que você digitou é um PALINDROMO!')

else:

    print('a frase que você digitou não é um PALINDROMO.')
