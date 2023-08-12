n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua outra nota:'))
m = (n1 + n2)/2
print('Sua media foi de {:.1f}'.format(m))
if m >= 6.0:
    print('Parabens não tiro nota baixa !')
else:
    print('Abaixo da media! Tente novamente.')