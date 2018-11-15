import math

ang = float(input('digite o angulo:'))
print(' o Angulo de {}, tem o seno de {:.2f} \n '
      'o coseno de {:.2f} \n'
      ' a tangente de {:.2f}'.format(ang, math.sin(math.radians(ang)),
                                    math.cos(math.radians(ang)),
                                    math.tan(math.radians(ang))))



