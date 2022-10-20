n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Só mais um: '))
if n1 / n2 > 1 and n1 / n3 > 1 and n2 / n3 > 1:
    print(f'Maior e menor valores digitados foram {n1} e {n3}')
elif n1 / n2 > 1 and n1 / n3 > 1 and n3 / n2 > 1:
    print(f'Maior e menor valores digitados foram  {n1} e {n2}')
elif n2 / n1 > 1 and n2 / n3 > 1 and n1 / n3 > 1:
    print(f'Maior e menor valores digitados foram {n2} e {n3}')
elif n2 / n1 > 1 and n2 / n3 > 1 and n3 / n1 > 1:
    print(f'Maior e menor valores digitados foram {n2} e {n1}')
elif n3 / n1 > 1 and n3 / n2 > 1 and n1 / n2 > 1:
    print(f'Maior e menor valores digitados foram {n3} e {n2}')
elif n3 / n1 > 1 and n3 / n2 > 1 and n2 / n1 > 1:
    print(f'Maior e menor valores digitados foram {n3} e {n1}')
else:
    print('Impossible! Quem diria!')