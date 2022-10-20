a = input('Digite algo: ')
#print('O tipo de {} é {}. Ele é alfabético? {} É númerico? {} É alfanumérico? {}'.format(a, type(a), a.isalpha(), a.isnumeric(), a.isalnum()))
print(f'O tipo de {a} é:\n {type(a)}.\n É alfabético? {a.isalpha()}.\n É numérico? {a.isnumeric()}.\n É alfanumérico? {a.isalnum()}.\n Está em maiúsculas? {a.isupper()}.\n Está em minúsculas? {a.islower()}.\n Está capitalizada? {a.istitle()}.')
