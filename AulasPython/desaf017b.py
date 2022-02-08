import math
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(x, y)
print('O valor da hipotenusa é {:.2f}'.format(hipo))



