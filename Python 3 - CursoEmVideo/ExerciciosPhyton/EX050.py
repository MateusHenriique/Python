soma = 0
pares = 0

for c in range(1, 7):
    
    numero = int(input('Digite o {}° numero: '.format(c)))

    if numero % 2 == 0:
        pares = pares + 1
        soma = soma + numero

print('Dos numero digitados {} são pares.'.format(pares))
print('A soma dos numeros pares é {}'.format(soma))