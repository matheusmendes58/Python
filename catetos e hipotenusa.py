from math import hypot
cco = float(input('comprimento do cateto oposto:'))  # cco comprimento cateto oposto
cca = float(input('Comprimento do cateto adijcente:'))   # comprimento cateto adjacente
print('A hipotenusa vai medir {:.2f}'.format(hypot(cco, cca)))
'''
calculo da hipotenusa sem a biblioteca 
hi = (cco ** 2 + cca) ** (1/2) 
lembrando que ** é = a potenciação 
'''

