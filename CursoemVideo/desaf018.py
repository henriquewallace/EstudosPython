import math
n = float(input('Digite um ângulo: '))
sin = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O seno do ângulo {}° é {:.2f}'.format(n, sin))
print('O cosseno do ângulo {}° é {:.2f}'.format(n, cos))
print('A tangente do ângulo {}° é {:.2f}'.format(n, tan))






