print('-=-'*35)
print('Bem vindo! Vou agora dizer entre dois números que você digitou o maior, menor, ou a igualdade, bora lá!')
print('-=-'*35)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O primeiro valor é maior!')
elif n2 > n1:
    print(f'O segundo valor é maior!')
else:
    print('Não existe valor maior, são iguais!')
