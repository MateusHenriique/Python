print('-=' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=' * 20)
reta_1 = float(input('Digite a 1° reta: '))
reta_2 = float(input('digite a 2° reta: '))
reta_3 = float(input('digite a 3° reta: '))

if (reta_1 + reta_2 > reta_3) and (reta_2 + reta_3 > reta_1) and (reta_3 + reta_1 > reta_2):
    
    if (reta_1 == reta_2) and (reta_2 == reta_3) and (reta_3 == reta_1):
        print('Estás retas formam um triangulo EQUILATERO')
    elif (reta_1 != reta_2) or (reta_2 != reta_3) or (reta_3 != reta_1):
        print('Estás retas formam um triangulo ISÓCELES')
    else:
        print('Estás retas formam um triangulo ESCALENO')

else:
    print('Essas retas não podem formar um triangulo.')
