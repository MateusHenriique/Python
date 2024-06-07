METROS = int(input('digite um valor em metros: '))
KM = METROS / 1000 
HM = METROS / 100
DAM = METROS / 10
DM = METROS / 10
CM = METROS * 100
MM = METROS * 1000
print('a medida de {} corresponde a: '.format(METROS))
print('em kilometros:  {} km'.format(KM))
print('em hectometro: {} hm'.format(HM))
print('em decametros: {} dam'.format(DAM))
print('em centimetros: {} cm'.format(CM))
print('em decimetros: {} dm'.format(DM))
print('em milimetros: {} mm'.format(MM))
