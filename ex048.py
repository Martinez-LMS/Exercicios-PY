nome = str(input('Qual seu nome ?'))
if nome == 'Leonardo':
    print('Que nome daora')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito comum...')
elif nome in 'Mayara':
    print('É o nome da minha namorada linda <3')
    print(' -=-' * 8)
else:
    print('Seu nome é chato... ')
    print(' -=-' *  8)
print('Tenha um bom dia, {}!'.format(nome))
print('-=-' * 10)