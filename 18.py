import math
n = (float(input('Digite o valor do ângulo: ')))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print(f'Seno = {(s):.2f} \nCosseno = {(c):.2f} \nTangente = {(t):.2f}')