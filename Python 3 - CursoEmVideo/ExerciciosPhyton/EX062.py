primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
continua = 10
vezes = 0
c = 0

while continua != 0:

    vezes += continua
    while c < vezes:

        print(primeiro, end=' -> ')
        primeiro += razao
        c += 1

    print('PAUSA')
    continua = int(input('Quantos termos você quer mostrar mais? '))

print('FIM... No total foram digitados {} termos.'.format(vezes))    
