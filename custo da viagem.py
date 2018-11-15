from time import sleep
d = float(input('Qual é a distancia da sua viagem?'))
print('--' * 20)
sleep(2)
if d <= 200:
    print('Você esta preste a começar a viagem de {}'
          '\nE o preço da sua passagem será de R${:.2f}'.format(d, d * 0.50))
else:
    print('Voçê esta preste a começar a viagem de {}'
          '\nE o preço da sua passagem será de R${:.2f}'.format(d, d * 0.45))
    print('lembrando que distancia acima de 200 KM é cobrado R$0.45 centavos ')


