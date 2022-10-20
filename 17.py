from math import sqrt, pow, hypot
a = float(input('Digite o valor do Cateto Oposto: '))
o = float(input('Digite o valor do Cateto Adjacente: '))
print(f'O valor da hipotenusa é {sqrt(pow(a, 2) + pow(o, 2)):.2f}')

#print(f'O valor da hipotenusa é {hypot(a, o)})
