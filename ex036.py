F = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(F.count('A')))
print('A primeira letra A apareceu na posição {}'.format(F.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(F.rfind('A')+1))