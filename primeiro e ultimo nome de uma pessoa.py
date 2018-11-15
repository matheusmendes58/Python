nome = str(input('digite seu nome:')).strip()
dividir = nome.split()
print('muito prazer em te conhecer !'
      '\nSeu primeiro nome é {}'
      '\nSeu ultimo nome é {}'.format(dividir[0], dividir[-1]))
'''
pode se colocar assim:
dividir[len(dividir)-1]
'''
