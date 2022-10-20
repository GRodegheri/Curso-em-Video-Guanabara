v = int(input('Digite a velocidade que o carro passou: '))
if v <= 80:
    print('Deu sorte menor, não vai tomar canetada!')
else:
    print(f'Deu ruim menor, vai tomar canetada no valor de {(v - 80)*7} reais')