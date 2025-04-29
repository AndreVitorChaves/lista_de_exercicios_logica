maior = menor = qnt = val = 0
a = 1
c = 1
nome = input('Olá usuário. Digite o seu nome: ')
while a == 1:
    n = int(input('{}, digite o {}º número: '.format(nome, c)))
    qnt += 1
    val += n
    c += 1
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor: 
            menor = n
    a = int(input('Digite 1 para continuar e 0 para encerrar: '))
print ('O maior valor dente esses números é {}.'.format(maior))
print ('O menor valor dentre esses números é {}.'.format(menor))
print('A média aritmética desses números é {}.'.format(val/qnt))