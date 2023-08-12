p1 = float(input('Primeiro segmento:'))
p2 = float(input('Segundo segmento:'))
p3 = float(input('Terceiro segmento:'))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima FORMAM UM TRIANGULO', end='')
    if p1 == p2 and p2 == p3:
        print('Equilatero !')
    elif p1 != p2 != p3 != p1:
            print('Escaleno !')
    else:
        print('Isoceles')
else:
    print('Os segmentos acima NÃO PODEM FORMA TRIANGULO')
