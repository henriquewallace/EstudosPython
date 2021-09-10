a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite mais um número: '))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))

