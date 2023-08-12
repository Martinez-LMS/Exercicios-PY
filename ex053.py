from datetime import date
atual = date.today().year
data = int(input('Ano de nascimento:'))
idade = atual - data
print('Quem nasceu em {} tem {} anos em {}.'.format(data, atual, idade))
if idade == 18:
    print('VOCE TEM QUE SE ALISTAR IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Voce nao tem 18 anos, falta {} anos'.format(saldo))
elif idade >18:
    saldo = idade - 18
    print('Voce deveria ter se alistado em {}'.format(saldo))
