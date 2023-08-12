p = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = p + (10 - 1) * razao
for c in range (p, decimo + razao, razao):
    print('{}'.format(c), end=(' -> '))
print('ACABOU')