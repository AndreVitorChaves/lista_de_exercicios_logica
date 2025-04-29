a = 1
while a == 1:
    n = int(input('Digite um número: '))
    for c in range(1, 11):
        print('{} X {} = {}'.format(n, c, n*c))
    a = int(input('Se deseja continuar, digite "1". Para encerrar, digite "0":\n'))
print('Obrigado por acessar nosso site, até mais!')