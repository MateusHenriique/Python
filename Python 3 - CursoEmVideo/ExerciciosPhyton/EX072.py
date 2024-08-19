contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    print('-='*20)
    str_numero = str(input('Digite um numero entre 0 e 20: ')).strip()
    
    if  str_numero.isdigit() == True:
        numero = int(str_numero)
           
        while numero < 0 or numero > 20:
            print('-='*20)
            print('Numero indisponivel, tente novamente...')
            print('-='*20)
            numero = int(input('Digite um numero entre 0 e 20: '))
        
        break
        
    else:
        print('-='*20)
        print('Não são permitidos caracteres como resposta... Tente novamente')

print('-='*20)
print(f'O numero digitado foi {contagem[numero]}')