print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)

primeiro_termo = int(input('digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):

    print(c, '-> ', end='')

print('ACABOU...')
