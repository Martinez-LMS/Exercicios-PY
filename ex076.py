print('Geradpr de PA')
print('-=' * 10)
primeiro = int(input('\033[1;33mPrimeiro termo:\033[m'))
razão = int(input('\033[1;34mRazao da PA\033[m'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end= '')
    termo += razão
    cont += 1
print('FIM')
