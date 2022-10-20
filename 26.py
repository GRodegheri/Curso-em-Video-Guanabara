a = input('Digite uma frase: ').strip()
a = a.lower()
print(f'''
A letra -a- aparece: {a.count('a')} vezes.
Aparece pela primeira vez na posição {a.find('a')+1}
E a última posição em que aparece é {a.rfind('a')+1}''')
