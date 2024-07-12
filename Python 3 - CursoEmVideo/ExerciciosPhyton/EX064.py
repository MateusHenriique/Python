valor = 0
totnun = 0
soma = 0
valor = int(input('Digite um valor [999 Para Parar]: '))

while valor != 999:

    soma = soma + valor
    totnun += 1
    valor = int(input('Digite um valor [999 Para Parar]: '))
    
print('No total foram digitados {} numeros. E a soma entro eles é : {}'.format(totnun, soma))
print('Programa Finalizado...')