sal = float(input('qual é o salario do funcionario: R$ '))
aumento = sal + (sal * 15 / 100)
print('o funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, aumento))
