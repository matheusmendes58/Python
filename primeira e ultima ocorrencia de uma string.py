frase = str(input('Digite uma frase:')).strip()
print('a letra A aparece {} vezes  na frase:'
      '\n A primeira letra A apareceu na posição {}'
      '\n A ultima letra A apareceu na posição {}'
      .format(frase.upper().count('A'), frase.upper().find('A') + 1,
              frase.upper().rfind('A') + 1))
