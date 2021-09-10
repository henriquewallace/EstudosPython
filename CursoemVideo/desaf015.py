km = float(input('Quantos km você percorreu com o carro? '))
d = int(input('Por quantos dias você utilizou o carro? '))
c = 60 * d
rod = 0.15 * km
t = c + rod
print('Você deve pagar um total de R${:.2f}.'.format(t))


