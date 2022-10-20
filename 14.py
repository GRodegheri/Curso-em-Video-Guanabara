temp = input('Qual temperatura você está tentando converter (F, C, K)? ')
if temp == 'K' or temp == 'kelvin':
    k = float(input('Digite o valor da temperatura: '))
    print(f'{k}K para celsius = {k - 273.15:.2f}ºC \n e para Fahrenheit {(k - 273.15)*(9/5)+32:.2f}ºF')
elif temp == 'F' or temp == 'Fahrenheit':
    f = float(input('Digite o valor da temperatura: '))
    print(f'{f}ºF para Celsius = {(f - 32) * (5 / 9):.2f}ºC \n e para Kelvin = {(f - 32) * (5 / 9) + 273.15:.2f}K ')
elif temp == 'C' or temp == 'Celsius':
    c = float(input('Digite a temperatura: '))
    print(f'{c}ºC para fahrenheit é = {((c * (9 / 5)) + 32):.2f} \n e para Kelvin = {c + 273.15:.2f}')
else:
    print('Larga de ser retardado!')
print('Obrigado por utilizar o termômetro Rodegheri!')