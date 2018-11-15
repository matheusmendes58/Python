nome = str(input('digite o nome do aluno: '))
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2)/2  # média
print('a média do {} entre {:.1f} e {:.1f} é igual a {:.1f} '.format(nome, n1, n2, m))
