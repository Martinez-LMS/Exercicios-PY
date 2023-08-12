from datetime import date
atual = date.today().year
totamaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu:'.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos '.format(idade))
    if idade >= 21:
        totamaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totamaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))
