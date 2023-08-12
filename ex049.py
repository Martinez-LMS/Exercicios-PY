casa = float(input('Valor da casa R$'))
salario = float(input('Salario do comprador R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de r${:.2f} em {} anos'.format(casa, anos), end= '')
print('A prestaçao sera de R$ {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser APROVADO')
else:
    print('Emprestimo NEGADO')