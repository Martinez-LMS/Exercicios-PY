n1 = int(input('Digite um numero, para saber seu Fatorial'))
c = n1
f = 1
while c > 0:
    print('{}'.format(c), end= '')
    print('x' if c > 1 else '=', end= '')
    f *= c
    c -= 1
print('O fatorial de {} é '.format(f, c))