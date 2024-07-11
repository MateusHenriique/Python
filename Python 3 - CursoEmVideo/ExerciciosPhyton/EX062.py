primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
continua = 1
vezes = 10

while continua != 0:

    c = 0
    while c < vezes:

        print(primeiro, end=' -> ')
        primeiro += razao
        c += 1

    print('PAUSA')
    vezes = int(input('Quantos termos você quer mostrar mais? '))
    continua = vezes

print('FIM')    
