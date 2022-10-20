#desafio 1 - nome + boas vindas
'''
# TODA FUNÇÃO TEM QUE TER PARENTESE

tipos primitivos
int / bool / float / string

print('A soma vale {}'.format{s}) #{} = MÁSCARA

print('A soma entre {} e {} vale {}'.format{n1, n2, s})

n = input('Digite algo: ')
print(n.isalpha()) print(n.isalnum()) print(n.isnumeric())

print(f'bla bla bla {variavel.comando}...)

OPERAÇÕES ARITMÉTICAS
+ = SOMA
- = SUBTRAÇÃO
* = MULTIPLICAÇÃO
/ = DIVISÃO
% = RESTO DA DIVISÃO
// = TRUNCAR DIVISÃO (SÓ A PARTE INTEIRA)
** = EXPONENCIAL OU POW(A, B)
Para escolher quantas casas depois da virgula {:.3f} ou seja, 3 casas flutuantes.
\n quebra linda e end=' ' une linhas ou prints separados
import / from import
quando usar import algo, tem que chamar a função usando algo.FUNÇÃO()
quando usar from import, pode chamar direto FUNÇÃO()

Manipulando cadeia de texto = frase (strings)
fatiamento de string

frase = 'curso em video python'
#c u r s o   e m   v i  d  e  o     p  y  t  h  o  n
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase[9] #maiúsculas != de minúsculas
V

frase[9:13] #Exclui o último termo (igual o from i in Range)
Vide

frase [9:21]
Video Python

frase[9:21:2] (espaçamento)
V d o P t o

frase[:5] quando não coloca onde começa, começa do caractere 0
Curso

frase[15:]
Python

frase[9::3]
V  e  P  h

ANALISE
len(frase) (length - comprimento)
21 

frase.count('o',0,13) #FAZ CONTAGEM COM FATIAMENTO

frase.find('deo')
em que posição começou das caixinhas (11)

frase.find('Android')
Retorna o valor -1 #significa que ela retornou uma função na existente na string

'Curso' in frase
True

- TRANSFORMAÇÃO
mudar cadeira des 

frase.replace('Python', 'Android')
frase.upper/lower() - todo método tem que ter () (maiusculo minusculo)
frase.capitalize() - difere do title ele pega a string inteira joga pra minusculo e somente a primeira letra da string ele converte para maiusculo
frase.title() - Joga cada primeira letra de cada palavra pra maiúsculo

frase = '   Aprenda Pythom  " para eliminar esses espaços desnecessários usar frase.strip() / frase.rstrip() [o r indica right, left, essas coisas]
frase.rstrip() frase.lstrip()

frase.Split() por padrão ele ataca os espaços entre palavras / cada splitador gera uma nova lista das palvras
'-'.join(frase - vai unir a frase por -) > 'Curso-em-Video-Python'

print(""" textos longos
que passem da linha
usar aspas triplas""")

replace   
print(frase.replace('python', 'android'))

frase.find('curso')
retorna 0 pq é a primeira casa em que começa

-----ESTRUTURAS CONDICIONAIS-----
ESTRUTURA SEQUENCIAL != ESTRUTURA CONDICIONAL
 COndicional simplificada
 a = int(input('Quantos anos tem seu carro? '))
 print ('carro novo' if a <=3 else 'carro velho')
 

CORES NO TERMINAL
PADRÃO ANSI ESCAPE SEQUENCE CONTRA BARRA COM CÓDIGO
\033[Estilo(sublinhada, essas coisas), Texto(), Backgroundm
exemplo --- \033[0;33;44m] ---
legenda \033[a;b;cm]
a - 0 - nenhum / 1 negrito / 4 sublinhado / 7 negativo
b - 30 branco / 31 vermelho / 32 verde / 33 amarelo / 34 azul / 35 roxo / 36 azul ciano / 37 cinza(padrão)
c - 40   =    / 41   =      / 42   =   / 43   =     / 44  =   / 45  =   / 46     =      / 47      =     
m - só deixar ele ali

PARTE PRÁTICA
print('olá, mundo!')
pra botar cor
print('\033[31mOlá, mundo!) #(cor vermelha)
e se você botar no fim o  comando da contra barra, ele termina a coloração no último caractere
print('\033[31mOlá, mundo!\033[m')
MODULO COLORISE
nome = 'Gabriel'
print(f'É um prazer te conhecer, {\033[m}{nome}{\033[m}!!!)

USANDO DICIONARIO
cores = {'limpa':'\033[m', 'azul':'\033[34m''}
print(f'É um prazer te conhecer, {'azul'}{nome}{'limpa'}!!!)

CONDIÇÕES ANINHADAS
if / elif / else








#nome = input('Digite o seu nome: ')
#print(f'Prazer em te conhecer {nome:>20}!') #> a direita < a esquerda ^ centralizado - se entrar um sinal antes, exemplo {nome:=>20} o nome fica com os sinais ao redor =====nome===== exemplo

import math
num = ('Digite um número')
raiz = math.sqrt(num)
print (f'A raiz de {num} é {math.floor(raiz)}') #ceil


import emoji
print(emoji.emojize('Olá, mundo :earth_americas:', language='alias'))
'''



