largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print ('para pintar essa parede voce precisara de {}L de tinta'.format(tinta))