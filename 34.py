s = float(input('Digite o valor do seu salário: '))
if s >= 1250:
    print(f'Seu novo salário é de R${s * 1.10}')
else:
    print(f'Seu novo salário é de R${s * 1.15}')
