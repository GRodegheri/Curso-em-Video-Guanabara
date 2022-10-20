from time import sleep
v = float(input('Digite o valor da casa: R$'))
s = float(input('Quanto você ganha? R$'))
t = int(input('Em quantos anos você quer pagar por ela? '))
vm = v / t
print(f'Sobre esses termos, o valor da sua parcela mensal será de R${(v / t):.2f}')
print('Carregando sua análise... ')
sleep(2)
if vm <= (s*0.3):
    print('''Parabéns, campeão, analisamos o seu salário e vimos que você tem condições de pagá-lo, portanto ele foi {}APROVADO{}'''.format('\033[32m', '\033[m'))
elif vm > (s*0.3):
    print('Desculpe, mas para essa parcela, seu empréstimo foi {}NEGADO{}'.format('\033[4;31m', '\033[m'))
