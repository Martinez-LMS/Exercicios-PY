n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é de {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('o aluno ficou de Recuperação')
elif media < 5:
    print('O aluno esta REPROVADO')
elif media >= 7:
    print('O aluno esta APROVADO')
