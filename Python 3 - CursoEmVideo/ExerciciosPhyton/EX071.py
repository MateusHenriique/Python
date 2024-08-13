'''crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte 
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-='*20)
print(f'{'CAIXA ELETRONICO':^40}')
print('-='*20)

saldo = 100
print(f'Saldo Disponivel: R${saldo}')

while True:
    
    print('-='*20)
    print('SAQUE    [1]')
    print('DEPOSITO [2]')
    print('CANCELAR [3]')
    opcao = int(input('Selecione a opção desejada:'))
    
    if opcao == 1:
        print('-='*20)
        saque = int(input('Quanto voce deseja sacar: '))
        
    if opcao == 2:
        print('-='*20)
        deposito = int(input('Quanto você deseja depositar: '))
        saldo += deposito
        print('-='*20)
        print(f'Saldo Disponivel: R${saldo}')
        
    if opcao == 3:
        break

print('Programa Finalizado!')