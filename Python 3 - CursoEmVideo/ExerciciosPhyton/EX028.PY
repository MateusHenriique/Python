import random

n_aduvinha = random.randint(1, 5)

from time import sleep

print('-=-' * 20)
print('vou pensar em um numero entre 1 e 5. tente adivinhar')
print('-=-' * 20)
sleep(2)
res = int(input('em que numero eu pensei? '))
print('processando...')
sleep(5)
if res == n_aduvinha:
    print('voce certou!!!')
else:
    print('errou!! eu tinha pensado em {}'.format(n_aduvinha))      
