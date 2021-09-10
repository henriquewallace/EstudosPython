d = float(input('Qual a distância da viagem em km? '))
pc = d * 0.5
pl = d * 0.45
if d<=200:
    print('O valor da passagem é de R${:.2f}.'.format(pc))
else:
    print('O valor da passagem é de R${:.2F}.'.format(pl))
print('Tenha uma boa viagem! ;)')
