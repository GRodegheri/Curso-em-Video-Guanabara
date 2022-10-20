
a = input('Digite seu nome completo: ')

print(f"""{a.upper().lstrip().rstrip()}
{a.lower().lstrip().rstrip()}
{len(''.join(a.split()))}
Primeiro nome: {a.split()[0]}, {len(a.split()[0])} letras. """)






