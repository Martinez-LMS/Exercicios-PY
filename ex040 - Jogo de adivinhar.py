from random import randint
from time import sleep
c = randint( 0, 6)
print('Pensei no numero {}.'.format(c)) #Faz o computador 'pensar'
print('-=-' * 12)
print(' Vou pensa em um numero entre 0 e 6.')
print('-=-' * 12 )
j = int(input('Em que numero pensei ?'))# jogador tenta adivinha
print('Carregando...')
sleep(2)
if j == c:
    print('Parabens você ganhou !')
else:
    print('Ganhei ! Eu pensei no numero {} e nao no {}'.format(c,j))

