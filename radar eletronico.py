v = float(input('Qual é a velocidade atual do carro?'))

if v > 80:
    multa = (v - 80) * 7
    print('Multado! Voçê excedeu o limite permitido que é de 80Km/h'
          '\nVoçê deve pagar  uma multa de R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança !')


