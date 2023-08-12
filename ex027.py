import random

n1 = int(input('digite um numero'))
n2 = int(input('Dgite outro numero'))
n3 = int(input('Digite outro numero'))
lista = [n1, n2, n3]
sorteado = random.choice(lista)
print ('o numero digitado foi {}'.format(sorteado))

#import random

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

lista = [n1, n2, n3]
escolhido = random.choice(lista)

print('O número escolhido foi {}'.format(escolhido))
