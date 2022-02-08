import math
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hipo = ((cato ** 2) + (cata ** 2)) ** (1/2)
print('O comprimento da hipotenusa é {}.'.format(hipo))


