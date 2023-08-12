n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))

print('\033[1;35m' + '=' * 35)
print('{:^35}'.format('MENU DE OPÇÕES'))
print('=' * 35 + '\033[m')

print('\033[1;36m[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA\033[m')

opção = str(input('\033[1;33mQual sua opção: \033[m'))

while opção != '5':
    if opção == '1':
        print('\033[1;32mA soma de {} e {} é igual a {}\033[m'.format(n1, n2, n1 + n2))
    elif opção == '2':
        print('\033[1;32mO produto de {} e {} é igual a {}\033[m'.format(n1, n2, n1 * n2))
    elif opção == '3':
        if n1 > n2:
            print('\033[1;32m{} é maior que {}\033[m'.format(n1, n2))
        elif n2 > n1:
            print('\033[1;32m{} é maior que {}\033[m'.format(n2, n1))
        else:
            print('\033[1;32mOs números são iguais\033[m')
    elif opção == '4':
        n1 = int(input('\033[1;33mPrimeiro valor: \033[m'))
        n2 = int(input('\033[1;33mSegundo Valor: \033[m'))
    else:
        print('\033[1;31mOpção inválida. Digite novamente.\033[m')

    print('\033[1;35m' + '=' * 35)
    print('{:^35}'.format('MENU DE OPÇÕES'))
    print('=' * 35 + '\033[m')

    print('\033[1;36m[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA\033[m')

    opção = str(input('\033[1;33mQual sua opção: \033[m'))

print('\033[1;31mPrograma encerrado. Obrigado por usar!\033[m')
