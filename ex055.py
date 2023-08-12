from datetime import date
atual = date.today().year
n = int(input('Ano de nascimento'))
idade = atual - n
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('mirim')
elif idade > 9 and idade <=14:
    print('Classifcação: INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('Senior')
else:
    print('Master')