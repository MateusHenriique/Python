primeiro = int(input('Digite o primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
termo = primeiro
c = 0

while c < 10:
 
    print(termo, end=' -> ')
    primeiro += razao_pa
    c += 1

print('FIM')
 