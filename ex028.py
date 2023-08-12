import random
n1 = str(input('Primeiro:'))
n2 = str(input('Segundo:'))
n3 = str(input('terceiro:'))

lista = [n1, n2, n3]
random.shuffle(lista)

print('a ordem sera:')
print(lista)

