n = float(input('uma distancia em metros: '))
km = n / 1000   # kilometros
hm = n / 100    # hectometros
dam = n / 10    # decametros
dm = n * 10     # decimetro
cm = n * 100    # centimetro
mm = n * 1000   # milimetros

print('A medida de {} corresponde\n {}km\n {}hm\n {}dam\n {}dm\n {}cm\n {}mm '.format(n, km, hm, dam, dm, cm, mm))
