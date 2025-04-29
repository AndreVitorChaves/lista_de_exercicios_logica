neg = 0
for c in range (0, 7):
    n = int(input('Digite o {}º valor: '.format(c + 1)))
    if (n<0):
        neg += 1
print('Entre os 7 valores, {} são negativos.'.format(neg))