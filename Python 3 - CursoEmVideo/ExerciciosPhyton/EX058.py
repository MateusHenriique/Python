from random import randint

print('Pensei em um numero de 0 a 10 Tente acertar: ')
adivinha = randint(0, 10)
tot_chutes = 0
acertou = False

while not acertou:

    palpite = int(input('Em qual numero eu Pensei? '))

    if palpite == adivinha:

        acertou = True

    elif palpite < adivinha:

        print('Mais... Tente outro numero: ')

    elif palpite > adivinha:

        print('Menos... Tente outro numero: ')

    tot_chutes += 1

print('ACERTOU! voche precisou de {} palpites para acertar!'.format(tot_chutes))
