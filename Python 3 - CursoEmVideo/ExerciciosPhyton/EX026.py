fease = str(input('digite alguma frase: ')).lower().strip()
print('a letra A aparece {} vezes na frase'.format(fease.count('a')))
print('a palavra A aparece primeiro na pocição: {}'.format(fease.find('a') + 1))
print('a palavra A aparece pela ultima vez na posição: {}'.format(fease.rfind('a') + 1))
#o .find pode ser lido usando o lado esquerdo ou o direito usando sua variação lfind, rfind