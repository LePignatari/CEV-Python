from math import cos, tan, sin, radians
ang = float(input('Informe um ângulo: °'))
print('O ângulo {} possui: '.format(ang))
print('Cosseno: {:.2f}'.format(cos(radians(ang))))
print('Seno: {:.2f}'.format(sin(radians(ang))))
print('Tangente: {:.2f}'.format(tan(radians(ang))))
