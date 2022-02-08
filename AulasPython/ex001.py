n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sobra = n1 % n2
print('A soma é {}, a subtração é {}.'.format(s, sub))
print('O produto é {}, a divisão é {:.3f}, a potência é {}'.format(m, d, e))
print('A divisão inteira é {} e a sobra da divisão é {}'.format(di, sobra))



