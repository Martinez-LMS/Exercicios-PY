v = float(input('Qual velocidade você esta ?'))
if v > 80:
    print('MULTADO, voce ultrapassou o limite que é 80km/h')
    multa = (v - 80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança')
