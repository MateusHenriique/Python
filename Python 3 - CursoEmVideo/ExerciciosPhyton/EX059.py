from time import sleep

escolha = 0
finalizar = 0

while finalizar != 5:

    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    escolha = 0

    while escolha != 4:

        print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Numeros
        [5] Sair do programa
        ''')
        escolha = int(input('Qual das opções voce deseja executar: '))  

        if escolha == 1:

            print('a soma dos dois numeros digitados é {}'.format(n1 + n2))
            sleep(2)

        elif escolha == 2:

            print('a multiplicação os 2 numeros digitados é: {}'.format(n1 * n2))
            sleep(2)

        elif escolha == 3:

            if n1 > n2:

                print('O maior numero digitado foi {}'.format(n1))
                sleep(2)

            else:

                print('O maior numero digitado foi {}'.format(n2))
                sleep(2)

        elif escolha == 4:

            print('Digite os novos numeros:  ')
        
        elif escolha == 5:

            escolha = 4
            finalizar = 5

        else:

            print('Escolha invalida')

print('Programa finalizado!')
