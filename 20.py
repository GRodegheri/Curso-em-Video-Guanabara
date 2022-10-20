import random
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
l = [a, b, c, d]
print(f'A ordem de apresentação dos trabalhos será: {random.sample(l, k = 4)}')