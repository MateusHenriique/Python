nota_1 = float(input('digite a primeira nota do aluno: '))
nota_2 = float(input('digite a segunda nota do aluno: '))
media = (nota_1 + nota_2) / 2
print('a media do aluno foi de: {}'.format(media))

if media < 5:
    print('Sua média foi {}, e é nota vermelha e está: REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}, e é nota abaixo da média e está: DE RECUPERAÇÂO!'.format(media))
else:
    print('Sua media foi {}, e é uma nota boa e está: APROVADO!'.format(media))