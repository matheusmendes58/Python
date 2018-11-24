n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))
# verificando menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('o menor numero é : {}'.format(menor))
# verificando maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o maior numero é : {}'.format(maior))
