print('{:=^40}'.format(' LOJA DO MARTI '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] A VISTA DINHEIRO/PIX
[2] A VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparç = int(input('Quanatas parcelas ?'))
    parcela = total / totparç
    print('Sua compra sera parcea em {}x de R$ {:.2f} COM juros'.format(totparç, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA de pagamento, tente novamente')