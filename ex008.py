n1  = int(input( 'um valor'))
n2 = int(input('outro valor'))
S = n1+n2
m = n1*n2
D = n1/n2
Di = n1//n2
E = n1**n2
print ('A soma vale {}, o produto vale {} e a divisão é {:.>3}'.format(S,m,D), end = '')
print ('Divisão inteira {} e potencia {}'.format(Di,E))