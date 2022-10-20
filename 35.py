from numpy import positive


a = int(input('Digite o valor de 3 seguimentos de reta e eu vou dizer se as medidas formam um triângulo.\nMEDIDA UM: '))
b = int(input('MEDIDA DOIS: '))
c = int(input('MEDIDA TRÊS: '))
if (b - c) < a and a < (b + c) and (b - a) < c and c < (b + a) and (a - c) < b and b < (a + c):
    print(f'As medidas {a}m, {b}m e {c}m formam um triângulo.')
else:
    print('Não forma triângulo.')