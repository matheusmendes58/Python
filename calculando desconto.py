n = float(input('qual o preço do produto R$:'))
x = n*5
d = x / 100  # d = desconto
print('O produto que custava R${}, na promoção de 5% vai custar R${:.2f}'.format(n, n - d))


