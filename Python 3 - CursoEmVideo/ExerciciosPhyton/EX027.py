nome = str(input('digite seu nome completo: ')).lower().strip()
nome = nome.split()
print('prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome) - 1])) #podemos ler uma serie de palavtas de tras para frente usando o len para ler e o -1 para identificarmos que quewremos ler começando da ultima palavra (passo -1)