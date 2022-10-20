a = input('qual o nome da sua cidade? ')
a = a.lower().strip #PENSE SEMPRE QUE O USUÁRIO VAI FAZER BESTEIRA NA HORA DE DIGITAR KKKKKKKKK
a = a.split()
if (a[0]) == 'santo':
    print('Sua cidade começa com a palavra Santo.')
else:
    print('Sua cidade não começa com a palavra Santo')
