a = float(input('Digite o comprimento de uma reta: '))
b = float(input('Digite o comprimento de outra reta: '))
c = float(input('Digite o comprimento de mais uma reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')
