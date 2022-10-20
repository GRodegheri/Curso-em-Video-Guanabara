dias = int(input('O carro ficou em sua posse por quantos dias? '))
km = float(input('Quantos km foi percorrido? '))
dp = dias * 60
kmp = km * 0.15
print(f'O carro ficou com você por {dias} dias e você rodou {km}km, logo, você pagará pelo serviço {dp + kmp:.2f}')