from random import randint
computador = randint(0, 10)
print('\033[1;34mSou seu computador.... Pensei em um número de 0 a 10')
print('Tente adivinhar qual é !\033[m')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('\033[1;33mQual seu palpite: \033[m'))
    palpite += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;31mMAIOR\033[m')
        elif jogador > computador:
            print('\033[1;31mMENOS\033[m')
print('\033[1;32mACERTOU com tantos {} palpites\033[m'.format(palpite))
