sal = float(input('Qual é o salario do funcionario? R$'))
au1 = sal + ((sal * 15) / 100)
au2 = sal + ((sal * 10) / 100)
if sal > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, au2))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, au1))

