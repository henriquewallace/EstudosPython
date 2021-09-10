v = float(input('Digite a velocidade do carro em km/h: '))
if v>80:
    print('Você ultrapassou o limite de velocidade de 80km/h em {}km/h'.format(v-80))
    print('Você pagará uma multa de R${:.2f}'.format((v-80) * 7))
else:
    print('Tenha um bom dia e dirija com segurança :)')

