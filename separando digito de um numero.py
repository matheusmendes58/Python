n = int(input('informe um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('analisando um numero:{} '.format(n))
print('unidade:{} '
      '\ndezena: {} '
      '\ncentena:{} '
      '\nmilhar: {}'
      .format(u, d, c, m))







