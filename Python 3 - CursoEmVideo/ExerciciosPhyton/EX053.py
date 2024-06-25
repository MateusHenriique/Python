frase = str(input('Digite uma frase: ')).strip().upper()
frase_2 = frase.split()
frase_3 = ''.join(frase_2)
palindromo = ''

for letra in range(len(frase_3) -1, -1, -1):

    palindromo = palindromo + frase_3[letra]

print('O inverso de {} é {}'.format(frase_3, palindromo))

if frase == palindromo:

    print('A frase que você digitou é um PALINDROMO!')

else:

    print('a frase que você digitou não é um PALINDROMO.')
