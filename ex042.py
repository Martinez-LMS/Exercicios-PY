d = float(input('Qual é a diatancia da viagem'))
print('Voce esta preste a começar uma viagem de {}km'.format(d))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(p))

'''p = d * 0.50 if d <= 200 else d * 0.45'''