n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
if n1 > n2:
    print('O valor maior é o PRIMEIRO {}'.format(n1))
elif n2 > n1:
    print('O SEGUNDO numero é maior {}'.format(n2))
else:
    print('Os dois valores são IGUAIS')