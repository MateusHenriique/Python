valor = int(input('Digite um valor: '))
res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
soma = valor
maior = valor
menor = valor
totvalores = 1

while res != 'N':

    valor = int(input('Digite um valor: '))
    res = str(input('Deseja continuar? [S/N]')).strip().upper()
    soma += valor
    totvalores += 1

    if menor < valor:

        menor = valor

    if maior > valor:

        maior = valor

media = soma / 2
print('-='*20)
print('Foram digitados {} valores.'.format(totvalores))
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))
print('A media dos valores digitaos foi: {}'.format(media))