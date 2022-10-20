import random
a = input('Digite o nome de um aluno: ')
b = input('Digite mais um: ')
c = input('Digite o terceiro: ')
d = input('Digite o último: ')
l = [a, b, c, d]
print(f'O aluno escolhido foi: {random.choice(l)}') 

