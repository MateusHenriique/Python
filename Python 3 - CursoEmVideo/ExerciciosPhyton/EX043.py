peso = float(input('digite o seu peso: (KG) '))
altura = float(input('qual é a sua altura: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('O seu IMC é {:.1f} e você está abaixo do Peso.'.format(imc))
elif imc > 18.5 and imc <= 25: 
    print('O seu IMC é {:.1f} e você está no peso Ideal.'.format(imc))
elif imc > 25 and imc <= 30: 
    print('O seu IMC é {:.1f} e você está com Sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40: 
    print('O seu IMC é {:.1f} e você está em estado de Obesidade.'.format(imc))
else: 
    print('O seu IMC é {:.1f} e você está em estado de Obesidade Mórbida.'.format(imc))


