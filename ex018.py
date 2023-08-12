preço = float(input('qual é op preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print ('o produto que custava r${}, na promoção com desconto de 5% vai custar r${}'.format(preço, novo))

# para descobrir o valor em percentage, basta usa a regra de 3,
# Ex: 10$ equivale a 100% do valor, não sabemos o que vale 5% por isso X
# 10 100% / x 5%