nome = str(input('digite seu nome:')).strip()
dividir = nome.split()
print('analisando seu nome...')
print('seu nome em maiusculo é :{}'.format(nome.upper()))
print('seu nome em minusculo é:{}'.format(nome.lower()))
print('seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem ao todo {} letras '.format(len(dividir[0])))



