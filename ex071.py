somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
for p in range(1, 5):

    print('----{} PESSOA ------'.format(p))
    nome = str(input('Nome')).strip()
    idade = input('idade')
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4
print('A media de idade de grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama `{}'.format(maioridadehomem, nomevelho))