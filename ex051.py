numero = int(input('Digite um numero'))
if  numero.isdigit() == 2:
    print('\033[1;32;40mGosto deste numero {}\033'.format(numero))
elif numero == 1 or 10:
    print('nao gosto destes numeros'.format(numero))
else:
    print('Este não é um numero !')
print('Gostei do seu numero'.format(numero))