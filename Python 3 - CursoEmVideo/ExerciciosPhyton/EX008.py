metros = int(input('digite um valor em metros: '))
km = metros / 1000 
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A medida de {} corresponde a: '.format(metros))
print('Em kilometros:  {} km'.format(km))
print('Em hectometro: {} hm'.format(hm))
print('Em decametros: {} dam'.format(dam))
print('Em centimetros: {} cm'.format(dm))
print('Em decimetros: {} dm'.format(cm))
print('Em milimetros: {} mm'.format(mm))
