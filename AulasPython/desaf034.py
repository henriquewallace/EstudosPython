s = float(input('Digite seu salário: R$'))
if s > 1250:
    print('Parabéns, você recebeu um aumento de 10%. Seu novo salário é R${:.2f}.'.format((s * 10) / 100 + s))
else:
    print('Parabéns, você recebeu um aumento de 15%. Seu novo salário é de R${:.2f}.'.format((s * 15) / 100 + s))
