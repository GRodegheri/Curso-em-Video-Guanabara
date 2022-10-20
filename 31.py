km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    print(f'Você vai pagar pela viagem R${km * 0.50}.')
else:
    print(f'Você vai pagar pela viagem R${km * 0.45}')
    