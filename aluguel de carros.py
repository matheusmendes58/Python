d = float(input('quantos dias alugados: '))
km = float(input('quantos KM rodados:'))
t = km * 0.15
print('O total a pagar é de R${:.2f}'.format(t + (d * 60)))

