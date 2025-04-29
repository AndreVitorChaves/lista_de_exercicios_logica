alturas = []
for i in range (1, 16):
    alt = float(input('Olá usuário, digite a sua altura em metros: '))
    alturas.append(alt)
menor = min(alturas)
maior = max(alturas)
print ('A menor altura do grupo é {}.'.format(min(alturas)))
print ('A maior altura do grupo é {}.'.format(max(alturas)))