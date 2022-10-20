from time import sleep
num = int(input('Digite um número qualquer: '))
esc = int(input('Digite 1 para binário\n2 para octal\n3 para hexadecimal: '))
print('Aguarde, estamos calculando...')
sleep(2)
if esc == 1:
    bin = bin(num)
    print(f'O binário de {num} é {bin}')
elif esc == 2:
    oct = oct(num)
    print(f'O Octal de {num} é {oct}')
elif esc == 3:
    hexa = hex(num)
    print(f'O Hexadecimal de {num} é {hexa}')
    
