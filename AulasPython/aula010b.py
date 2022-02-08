n1 = float(input('Digite sua nota em português: '))
n2 = float(input('Digite sua nota em matemática: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m <6:
    print('Você foi reprovado')
else:
    print('Parabéns! Você foi aprovado.')
print('--FIM--')
