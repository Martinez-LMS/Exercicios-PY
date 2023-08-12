import math

an = float(input('Digite um angulo que voce deseja:'))
seno = math.sin(math.radians(an))
print ('O angulo de {} tem SENO de {:.2f}'.format(an, seno))
co = math.cos(math.radians(an))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(an,co))
tan = math.tan(math.radians(an))
print ('o angulo de {} tem o tangente de {:.2f}'.format(an,tan))