from random import randint
from time import sleep  # congelamento de tempo ()segundos
n = randint(0, 5)   # maquina randomiza de 1 a 5  esses dois numeros
print('-=-' * 20)
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar')
print('-=-' * 20)
x = int(input('Em que numero eu pensei?'))  # jogador tenta adivinhar
print('PROCESSANDO')
sleep(2)
if x == n:
    print('PARABENS você me vençeu')
else:
    print('GANHEI eu pensei no número {} e não no número {}'.format(n, x))



