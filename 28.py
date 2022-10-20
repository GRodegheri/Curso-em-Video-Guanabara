from random import randint
from time import sleep
while True: 
    a = randint(0,5)
    print('-=-' *11)
    print('Vou pensar em um número de 0 a 5!')
    print('-=-' *11)
    b = int(input('Adivinhe que número eu pensei: '))
    print('PROCESSANDO MENÓ, CALMA AI CRIA...')
    sleep(2)
    if b != a:
        print('Eroooooooooooou')
    else:
        print('Acertoooooou cria. lançou a braba')
        break
        

