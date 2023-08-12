n = cont = soma = 0
n = int(input('Digite um numero [999 para parar]'))

while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um numero [999 para parar]'))
print('Voce digitou {} numeros e a soma entres foi {}'.format(cont, soma))