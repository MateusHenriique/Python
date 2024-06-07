real = float(input('Digite o valor em real que voce tem: R$'))
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(real, (real / 5.29)))