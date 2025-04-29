conti = 1
sal1 = 0
sal2 = 0
filhos2 = 0
filhos3 = 0
sal_maior = 0
sal_perc = 0
while conti == 1:
    nome = input('Olá usuário, digite o seu nome: ')
    sal = float(input('Caro, {}, digite o seu salário em reais: R$'))
    sal1 += sal
    sal2 += 1
    if sal>sal_maior:
        sal_maior = sal
    if sal <= 1000.00:
        sal_perc += 1
    filhos = input('Perfeito, {}, agora nos diga, você tem filhos?\n a) Sim \n b)Não\n ' ).lower()
    if (filhos == 'a'):
        filhos1 = int(input('Certo, quantos filhos(a) você tem? ' ))
    else:
        filhos1 = 0
    filhos2 += filhos1
    filhos3 += 1
    conti = int(input('Caro(a) usuário, pesquisa encerrada. Deseja continuar?\n Digite "1" para continuar. Digite "0" para encerrar\n'))
print('Muito obrigado pela atenção. Fique com os resultados da pesquisa: ')
sal_med = sal1/sal2
filhos_med = filhos2/filhos3
porcent_sal = (sal2/sal_perc)*100
print(sal_med)
print(filhos_med)
print(sal_maior)
print(porcent_sal)






