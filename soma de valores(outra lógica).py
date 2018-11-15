n1 = int(input('digite o primeiro valor: '))
print(type(n1))
#comando type mostra o tipo primitivo da variavel se é string
#ou float ou int e etc.
n2 = int(input('digite o segundo valor: '))
print(type(n2))
s = n1+n2
#s = soma
#print('a soma entre', n1, 'e', n2, 'é: ', s)
#primeiro metedo acima para dar print
print('a soma entre {} e {} é {}'.format(n1, n2, s))
#segundo método é mais facil
