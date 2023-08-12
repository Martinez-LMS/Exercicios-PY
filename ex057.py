peso = input('Qual é seu peso (KG): ')
altura = input('Qual é sua altura (metros): ')

if ',' in peso or ',' in altura:
    print('Não utilize vírgula como separador decimal. Utilize ponto (.)')
    exit()

peso = float(peso)
altura = float(altura)
imc = peso / (altura ** 2)

print('-=-' * 10)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso NORMAL')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso IDEAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
else:
    print('Valores inválidos para peso e/ou altura')

print('-=-' * 10)
