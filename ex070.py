maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa:'.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('0 maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))
