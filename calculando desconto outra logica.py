preco = float(input('Qual é o preço do produto R$:'))
desconto = preco - (preco * 5 / 100)
print('O preço do produto R${}, na promoção de 5% de desconto fica R${:.2f}'.format(preco, desconto))
