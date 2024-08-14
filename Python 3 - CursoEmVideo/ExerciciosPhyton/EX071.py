print('-='*20)
print(f'{'CAIXA ELETRONICO':^40}')
print('-='*20)

saldo = 100
print(f'Saldo Disponivel: R${saldo}')
tot_50 = tot_20 = tot_10 = tot_1 = 0


while True:
    
    print('-='*20)
    print('SAQUE    [1]')
    print('DEPOSITO [2]')
    print('CANCELAR [3]')
    opcao = int(input('Selecione a opção desejada:'))
    
    if opcao == 1:
        print('-='*20)
        saque = int(input('Quanto voce deseja sacar: '))
        
        if saldo - saque < 0:
            print('-='*20)
            print('Saldo insuficiente, operacão cancelada.')
            
        else:
            
            saldo -= saque
            troco = saque
            
            while True:
                
                if troco != 0:
                    if troco >= 50:
                        troco -= 50
                        tot_50 += 1
                            
                    elif troco >= 20:
                        troco -= 20 
                        tot_20 += 1
                        
                    elif troco >= 10:
                        troco -= 10
                        tot_10 += 1
                        
                    elif troco >= 1:
                        troco -= 1
                        tot_1 += 1
                
                else:
                    break
        
            print('-='*20)            
            print(f'valor de saque solicitado: R${saque}')
            print(f'sera sacado {tot_50} notas de R$50, {tot_20} notas de R$20, {tot_10} notas de R$10 e {tot_1} moedas de R$1')     
              
        print('-='*20)
        print(f'Saldo Disponivel: R${saldo}') 
            
    if opcao == 2:
        print('-='*20)
        deposito = int(input('Quanto você deseja depositar: '))
        saldo += deposito
        print('-='*20)
        print(f'Saldo Disponivel: R${saldo}')
        
    if opcao == 3:
        break

print('-='*20)
print('Programa Finalizado!')