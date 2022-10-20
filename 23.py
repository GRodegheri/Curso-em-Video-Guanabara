a = int(input('Digite um número de 0 a 9999: '))
print(f'''Unidade: {a // 1 % 10}
    Dezena: {a // 10 % 10}
    Centena: {a // 100 % 10}
    Milhar: {a // 1000 % 10}''') 



