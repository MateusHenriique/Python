metros = int(input('digite um valor em metros: '))
km = metros / 1000 
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('a medida de {} corresponde a: '.format(metros))
print('em kilometros:  {} km'.format(km))
print('em hectometro: {} hm'.format(hm))
print('em decametros: {} dam'.format(dam))
print('em centimetros: {} cm'.format(dm))
print('em decimetros: {} dm'.format(cm))
print('em milimetros: {} mm'.format(mm))
