n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')

print('\033[m')  # Resetar a cor para o padrão
print('O número {} foi divisível {} vezes'.format(n, tot))

if tot == 2:
    print('\033[34mE por isso ele É PRIMO')
else:
    print('\033[31mE por isso ele NÃO É PRIMO')
