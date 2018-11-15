n1 = float(input('quanto dinheiro voçê tem na carteira R$ : '))
n2 = n1 / 3.88
n3 = float(input('digite o valor em dolares U$:'))
print('Com R${:.2f} você pode comprar U${:.2f} dolares'.format(n1, n2))
print('a conversão de U${:.2f} para R${:.2f}'.format(n3, (n3*3.88)))




