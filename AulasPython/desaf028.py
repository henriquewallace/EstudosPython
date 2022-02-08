from random import randint
from time import sleep
n = int(input('Tente advinhar qual o número inteiro entre 0 e 5 foi escolhido pelo adversário: '))
r = randint(0, 5)
print('PROCESSANDO...')
sleep(1.5)
if n == r:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente :)')
print('O número escolhido foi {}'.format(r))





